# SPDX-FileCopyrightText: 2017-2021 Alliander N.V. <korte.termijn.prognoses@alliander.com> # noqa E501>
#
# SPDX-License-Identifier: MPL-2.0
import json
import os
from abc import ABC, abstractmethod
from datetime import datetime
from json import JSONDecodeError
from pathlib import Path
from typing import List, Optional, Union, Tuple
from urllib.parse import unquote, urlparse

import joblib
import mlflow
import pandas as pd
import pytz
import structlog
from matplotlib import figure
from mlflow.exceptions import MlflowException
from mlflow.tracking import MlflowClient
from openstf_dbc.services.prediction_job import PredictionJobDataClass
from plotly import graph_objects

from openstf.data_classes.model_specifications import ModelSpecificationDataClass
from openstf.metrics.reporter import Report
from openstf.model.regressors.regressor import OpenstfRegressor

MODEL_FILENAME = "model.joblib"
FOLDER_DATETIME_FORMAT = "%Y%m%d%H%M%S"
MODEL_ID_SEP = "-"
MAX_N_MODELS = 10  # Number of models per experiment allowed in model registry
E_MSG = "feature_names couldn't be loaded, using None"


class AbstractSerializer(ABC):
    def __init__(self, trained_models_folder: Union[Path, str]) -> None:
        """

        Args:
            trained_models_folder (Path): path to save models to
        """
        path = os.path.abspath(f"{trained_models_folder}/mlruns/")
        self.mlflow_folder = Path(path).as_uri()
        self.logger = structlog.get_logger(self.__class__.__name__)
        self.trained_models_folder = trained_models_folder
        self.client = None
        self.logger.debug(f"MLflow path at init= {self.mlflow_folder}")

    @abstractmethod
    def save_model(self, model: OpenstfRegressor) -> None:
        """Persists trained sklearn compatible model

        Args:
            model: Trained sklearn compatible model object
        """
        self.logger.error("This is an abstract method!")

    @abstractmethod
    def load_model(
        self, pid: Union[str, int]
    ) -> Tuple[OpenstfRegressor, ModelSpecificationDataClass]:
        """Loads model that has been trained earlier

        Returns: Trained sklearn compatible model object

        """
        self.logger.error("This is an abstract method!")


class PersistentStorageSerializer(AbstractSerializer):
    def save_model(
        self,
        model: OpenstfRegressor,
        pj: PredictionJobDataClass,
        modelspecs: ModelSpecificationDataClass,
        report: Report,
        phase: str = "training",
        **kwargs,
    ) -> None:
        """Save sklearn compatible model to persistent storage with MLflow.

            Either a pid or a model_id should be given. If a pid is given the model_id
            will be generated.

        Args:
            model (OpenstfRegressor): Trained sklearn compatible model object.
            pj (PredictionJobDataClass): Prediction job.
            modelspecs (ModelSpecificationDataClass): Dataclass containing model specifications
            report (Report): Report object.
            phase (str): Where does the model come from, default is "training"
            **kwargs: Extra information to be logged with mlflow, this can add the extra modelspecs

        """
        experiment_id = self.setup_mlflow(pj["id"])
        try:
            # return the latest run of the model can be phase tag = training or hyperparameter tuning
            prev_run = mlflow.search_runs(
                experiment_id,
                filter_string=" attribute.status = 'FINISHED' AND tags.mlflow.runName = '{}'".format(
                    pj["model"]
                ),
                max_results=1,
            )
            # Use [0] to only get latest run id
            prev_run_id = str(prev_run["run_id"][0])
        except LookupError:
            self.logger.info("No previous model found in MLflow", pid=pj["id"])
            prev_run_id = None
        with mlflow.start_run(run_name=pj["model"]):
            self._log_model_with_mlflow(
                pj, modelspecs, model, report, phase, prev_run_id, **kwargs
            )
            self._log_figure_with_mlflow(report)
        self.logger.debug(f"MLflow path after saving= {self.mlflow_folder}")

    def load_model(
        self,
        pid: Union[str, int],
        model_id: Optional[str] = None,
    ) -> Tuple[OpenstfRegressor, ModelSpecificationDataClass]:
        """Load sklearn compatible model from persistent storage.

            If a pid is given the most recent model for that pid will be loaded.

        Args:
            modelspecs (ModelSpecificationDataClass): Dataclass containing model specifications
            model_id (Optional[str], optional): Model id. Defaults to None. Used when MLflow didn't work.


        Raises:
            AttributeError: when there is no experiment with pid in MLflow
            LookupError: when there is no model in MLflow
            OSError: When directory doesn't exist
            MlflowException: When MLflow is not able to log

        Returns:
            OpenstfRegressor: Loaded model
            ModelSpecificationDataClass: model specifications
        """
        # create basic modelspecs
        modelspecs = ModelSpecificationDataClass(id=pid)

        try:
            experiment_id = self.setup_mlflow(pid)
            # return the latest run of the model, .iloc[0] because it returns a list with max_results number of runs
            latest_run = mlflow.search_runs(
                experiment_id,
                filter_string="attribute.status = 'FINISHED'",
                max_results=1,
            ).iloc[0]

            loaded_model = mlflow.sklearn.load_model(
                os.path.join(latest_run.artifact_uri, "model/")
            )

            # get the parameters from the old model, we insert these later into the new model
            # get the hyper parameters from the previous model
            modelspecs.hyper_params = loaded_model.get_params()
            # get used feature names else use all feature names
            modelspecs.feature_names = self._get_feature_names(
                pid, latest_run, modelspecs, loaded_model
            )

            # Add model age to model object
            loaded_model.age = self._determine_model_age_from_mlflow_run(latest_run)
            # URI containing file:/// before the path
            uri = os.path.join(latest_run.artifact_uri, "model/")
            # Path without file:///
            loaded_model.path = unquote(urlparse(uri).path)
            self.logger.info("Model successfully loaded with MLflow")
            return loaded_model, modelspecs
        # Catch possible errors
        except (AttributeError, LookupError, MlflowException, OSError) as e:
            self.logger.warning(
                "Couldn't load with MLflow, trying the old way",
                pid=pid,
                error=e,
            )
            return self.load_model_no_mlflow(pid, model_id), modelspecs

    def load_model_no_mlflow(
        self, pid: Optional[Union[int, str]] = None, model_id: Optional[str] = None
    ) -> OpenstfRegressor:
        """Load sklearn compatible model from persistent storage.

            Either a pid or a model_id should be given. If a pid is given the most
            recent model for that pid will be loaded.

        Args:
            pid (Optional[Union[int, str]], optional): Prediction job id. Defaults to None.
            model_id (Optional[str], optional): Model id. Defaults to None.

        Raises:
            ValueError: When both or none of pid and model_id are given.
            FileNotFoundError: When the model does not exist

        Returns:
            OpenstfRegressor: Loaded model
        """
        if pid is None and model_id is None:
            raise ValueError("Need to supply either a pid or a model_id")
        if pid is not None and model_id is not None:
            raise ValueError("Cannot supply both a pid and a model_id")
        if pid is not None:
            model_path = self.find_most_recent_model_path(pid)
        else:
            model_path = self.convert_model_id_into_model_path(model_id)
        if model_path is None:
            msg = f"No (most recent) model found"
            self.logger.error(msg)
            raise FileNotFoundError(msg)
        if model_path.is_file() is False:
            msg = f"model_path is not a file ({model_path})"
            self.logger.error(msg)
            raise FileNotFoundError(msg)
        return self.load_model_from_path(model_path)

    @staticmethod
    def save_model_to_path(model_path: Union[Path, str], model: OpenstfRegressor):
        joblib.dump(model, model_path)

    def load_model_from_path(self, model_path: Union[Path, str]) -> OpenstfRegressor:
        # Load most recent model from disk
        try:
            self.logger.debug(f"Trying to load model from: {model_path}")
            loaded_model = joblib.load(model_path)
        except Exception as e:
            self.logger.error("Could not load most recent model!", exception=str(e))
            raise FileNotFoundError("Could not load model from the model file!")

        # extract model age
        model_age_in_days = float("inf")  # In case no model is loaded,
        # we still need to provide an age
        if loaded_model is not None:
            model_age_in_days = self._determine_model_age_from_path(model_path)

        # Add model age to model object
        loaded_model.age = model_age_in_days
        loaded_model.path = model_path
        self.logger.info("Model loaded")
        return loaded_model

    def determine_model_age_from_pid(self, pid: int) -> float:
        """Determine model age in days of most recent model for a given pid.
        If no previous model is found, float(Inf) is returned

        Args:
            pid: int

        Returns:
            float: model age in days"""
        model_path = self.find_most_recent_model_path(pid)
        if model_path is not None:
            model_age_days = self._determine_model_age_from_path(model_path)
        else:
            model_age_days = float("Inf")
        return model_age_days

    def _determine_model_age_from_path(self, model_path: Path) -> float:
        """Determines how many days ago a model is trained base on the folder name.

        Args:
            model_path: pathlib.Path: Path to the model folder

        Returns: Number of days since training of the model

        """

        # Location is of this format: TRAINED_MODELS_FOLDER/<pid>/<YYYYMMDDHHMMSS>/
        datetime_string = model_path.parent.name

        # Convert string to datetime object
        try:
            model_datetime = datetime.strptime(datetime_string, FOLDER_DATETIME_FORMAT)
        except Exception as e:
            self.logger.warning(
                "Could not parse model folder name to determine model age. Returning infinite age!",
                exception=e,
                folder_name=datetime_string,
            )
            return float("inf")  # Return fallback age

        # Get time difference between now and training in days
        model_age_days = (datetime.utcnow() - model_datetime).days

        return model_age_days

    # noinspection PyPep8Naming
    def _determine_model_age_from_mlflow_run(self, run: pd.Series) -> Union[int, float]:
        """Determines how many days ago a model is trained from the mlflow run

        Args:
            run (mlfow run): run containing the information about the trained model

        Returns:
            model_age_days (int): age of the model
        """
        try:
            model_datetime = run.end_time.to_pydatetime()
            model_datetime = model_datetime.replace(tzinfo=None)
            model_age_days = (datetime.utcnow() - model_datetime).days
        except Exception as e:
            self.logger.warning(
                "Could not get model age. Returning infinite age!",
                exception=e,
                time=run.end_time,
            )
            return float("inf")  # Return fallback age
        return model_age_days

    def find_model_folders(
        self, pid: Union[int, str], ascending: Optional[bool] = False
    ) -> List[Path]:
        pid_model_folder = Path(self.trained_models_folder) / f"{pid}"

        # Declare empty list to append folder names
        model_folders = []

        if pid_model_folder.is_dir() is False:
            return model_folders

        for folder in pid_model_folder.iterdir():
            # Skip files, we are looking for folders
            if folder.is_dir() is False:
                continue
            # model folders should start with a 2 (date starts with 2000s)
            if folder.name.startswith("2") is False:
                continue
            # the model folder is only valid when there is a valid model file
            if (folder / MODEL_FILENAME).is_file() is False:
                continue
            model_folders.append(folder)

        model_folders = sorted(model_folders, reverse=not ascending)

        return model_folders

    def find_model_paths(
        self,
        pid: Union[int, str],
        limit: Optional[int] = 1,
        ascending: Optional[bool] = False,
    ) -> List[Path]:
        model_paths = [
            f / MODEL_FILENAME for f in self.find_model_folders(pid, ascending)
        ]

        model_paths = model_paths[:limit]

        return model_paths

    def find_most_recent_model_folder(self, pid: Union[int, str]) -> Union[Path, None]:
        """Find the model recent model folder.

            Iterate over the directories in the 'pid' model folder (the top level model
            folder for a specific pid) and find the
            <trained_models_folder>/<pid>/<datetime>

        Args:
            pid (Union[int, str]): Prediction job id.

        Returns:
            Union[pathlib.Path, None]: Path to the most recent model file or None if not
                found.
        """

        model_folders = self.find_model_folders(pid, ascending=False)

        if len(model_folders) == 0:
            return None

        # return the first model folder (ascending order)
        return model_folders[0]

    def find_most_recent_model_path(self, pid: Union[int, str]) -> Union[Path, None]:
        model_folder = self.find_most_recent_model_folder(pid)
        if model_folder is None:
            return None
        return self.find_most_recent_model_folder(pid) / MODEL_FILENAME

    def convert_model_id_into_model_folder(self, model_id: str) -> Path:
        """Convert a trained model id into a model folder.

            The model_id should use the following format:
                "<prediction_job_id>/<datetime>"

        Args:
            model_id ([type]): [description]
        """
        base_path = self.trained_models_folder

        prediction_job_id, model_datetime = model_id.split(MODEL_ID_SEP)

        return Path(base_path) / prediction_job_id / model_datetime

    def convert_model_id_into_model_path(self, model_id):
        return self.convert_model_id_into_model_folder(model_id) / MODEL_FILENAME

    @staticmethod
    def generate_model_id(pid: Union[int, str]) -> str:
        now = datetime.now(pytz.utc).strftime(FOLDER_DATETIME_FORMAT)
        model_id = f"{pid}{MODEL_ID_SEP}{now}"
        return model_id

    def setup_mlflow(self, pid: Union[int, str]) -> str:
        """Setup MLflow with a tracking uri and create a client

        Args:
            pid (int): Prediction job id

        Returns:
            int: The experiment id of the prediction job

        """
        # Set a folder where MLflow will write to
        mlflow.set_tracking_uri(self.mlflow_folder)
        # Setup a client to get the experiment id
        self.client = MlflowClient()
        mlflow.set_experiment(str(pid))
        self.logger.debug(f"MLflow path during setup= {self.mlflow_folder}")
        return self.client.get_experiment_by_name(str(pid)).experiment_id

    def _log_model_with_mlflow(
        self,
        pj: PredictionJobDataClass,
        modelspecs: ModelSpecificationDataClass,
        model: OpenstfRegressor,
        report: Report,
        phase: str,
        prev_run_id: str,
        **kwargs,
    ) -> None:
        """Log model with MLflow

        Args:
            pj (PredictionJobDataClass): Prediction job
            model (OpenstfRegressor): Model to be logged
            report (Report): report where the info is stored
            phase (str): Origin of the model (Training or Hyperparameter_opt)
            prev_run_id (str): Run-id of the previous run in this prediction job
            **kwargs: Extra information to be logged with mlflow

        """

        # Set tags to the run, can be used to filter on the UI
        mlflow.set_tag("run_id", mlflow.active_run().info.run_id)
        mlflow.set_tag("phase", phase)
        mlflow.set_tag("Previous_version_id", prev_run_id)
        mlflow.set_tag("model_type", pj["model"])
        mlflow.set_tag("prediction_job", pj["id"])

        # add modelspecs attributes except hyper_params

        # save feature names and target to MLflow, assume target is the first column
        mlflow.set_tag("feature_names", modelspecs.feature_names[1:])
        mlflow.set_tag("target", modelspecs.feature_names[0])

        # Add metrics to the run
        mlflow.log_metrics(report.metrics)
        # Add the used parameters to the run + the params from the prediction job
        modelspecs.hyper_params.update(model.get_params())
        mlflow.log_params(modelspecs.hyper_params)

        # Process args
        for key, value in kwargs.items():
            if isinstance(value, dict):
                mlflow.log_dict(value, f"{key}.json")
            elif isinstance(value, str) or isinstance(value, int):
                mlflow.set_tag(key, value)
            elif isinstance(value, graph_objects.Figure):
                mlflow.log_figure(value, f"figures/{key}.html")
            elif isinstance(value, figure.Figure):
                mlflow.log_figure(value, f"figures/{key}.png")
            else:
                self.logger.warning(
                    f"Couldn't log {key}, {type(key)} not supported", pid=pj["id"]
                )

        # Log the model to the run
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",
            signature=report.signature,
        )
        self.logger.info("Model saved with MLflow", pid=pj["id"])

    def _log_figure_with_mlflow(self, report) -> None:
        """Log model with MLflow

        Args:
            report (Report): report where the info is stored

        """
        # log reports/figures in the artifact folder

        if report.feature_importance_figure is not None:
            mlflow.log_figure(
                report.feature_importance_figure, "figures/weight_plot.html"
            )

        for key, fig in report.data_series_figures.items():
            mlflow.log_figure(fig, f"figures/{key}.html")
        self.logger.info(f"logged figures to MLflow")

    def _find_all_models(self, pj: PredictionJobDataClass):
        experiment_id = self.setup_mlflow(pj["id"])
        prev_runs = mlflow.search_runs(
            experiment_id,
            filter_string=" attribute.status = 'FINISHED' AND tags.mlflow.runName = '{}'".format(
                pj["model"]
            ),
        )
        return prev_runs

    def remove_old_models(
        self, pj: PredictionJobDataClass, max_n_models: int = MAX_N_MODELS
    ):
        """Remove old models for the experiment defined by PJ.
        A maximum of 'max_n_models' is allowed"""
        if max_n_models < 1:
            raise ValueError(
                f"MAX_N_MODELS should be greater than 1! Received: {max_n_models}"
            )

        prev_runs = self._find_all_models(pj)

        if len(prev_runs) > max_n_models:
            self.logger.debug(
                f"Going to delete old models. {len(prev_runs)}>{max_n_models}"
            )
            # Find run_ids of oldest runs
            runs_to_remove = prev_runs.sort_values(by="end_time", ascending=False).loc[
                max_n_models:, :
            ]
            for _, run in runs_to_remove.iterrows():
                self.logger.debug(f"Removing run {run.run_id}, from {run.end_time}")
                mlflow.delete_run(run.run_id)

    def _get_feature_names(
        self,
        pid: Union[int, str],
        latest_run: pd.Series,
        modelspecs: ModelSpecificationDataClass,
        loaded_model: OpenstfRegressor,
    ) -> Optional[list]:
        """Get the feature_names from MLflow or the old model

        Args:
            pid: prediction job id
            latest_run: pandas series of the last MLflow run
            modelspecs: model specification
            loaded_model: previous model

        Returns:
            list: feature names to use
        """
        try:
            modelspecs.feature_names = json.loads(
                latest_run["tags.feature_names"].replace("'", '"')
            )

        except KeyError:
            self.logger.warning(
                E_MSG,
                pid=pid,
                error="tags.feature_names, doesn't exist in run",
            )
        except AttributeError:
            self.logger.warning(
                E_MSG,
                pid=pid,
                error="tags.feature_names, needs to be a string",
            )
        except JSONDecodeError:
            self.logger.warning(
                E_MSG,
                pid=pid,
                error="tags.feature_names, needs to be a string of a list",
            )

        # todo: this code should become absolute after a few runs
        # if feature names is non see if we can retrieve them from the old model
        if modelspecs.feature_names is None:
            try:
                if loaded_model.feature_names is not None:
                    modelspecs.feature_names = loaded_model.feature_names
                    self.logger.info(
                        "feature_names retrieved from old model with an attribute",
                        pid=pid,
                    )
            except AttributeError:
                self.logger.warning(
                    "feature_names not an attribute of the old model, using None ",
                    pid=pid,
                )
        return modelspecs.feature_names
