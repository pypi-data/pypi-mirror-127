import os
import logging
import logging.config
from pathlib import Path

from bunch import Bunch
from azureml.core import Experiment, Workspace
from azureml.core.run import Run

from .utils import download_dataset, get_dataset_path

DATA_DIR_ONLINE_RUN = Path("/tmp/data/")
REPO_DIR = Path(__file__).parents[3].absolute()


class RunInitializer:
    """Setup AzureML and prepare dataset"""
    def __init__(self, data_config: Bunch, eval_config: Bunch):
        self._data_config = data_config
        self._eval_config = eval_config
        self.run_azureml_setup()
        self.get_dataset()

    def run_azureml_setup(self):
        raise NotImplementedError

    def get_dataset(self):
        raise NotImplementedError


class OfflineRunInitializer(RunInitializer):
    """Offline run. Download the sample dataset and run locally. Still push results to Azure"""
    def __init__(self, data_config: Bunch, eval_config: Bunch):
        super().__init__(data_config, eval_config)

    def run_azureml_setup(self):
        logging.info("Running in offline mode...")
        logging.info("Accessing workspace...")
        self.workspace = Workspace.from_config()
        self.experiment = Experiment(self.workspace, self._eval_config.EXPERIMENT_NAME)
        self.run = self.experiment.start_logging(outputs=None, snapshot_directory=None)

    def get_dataset(self):
        logging.info("Accessing dataset...")
        dataset_name = self._data_config.NAME
        self.dataset_path = str(REPO_DIR / "data" / dataset_name)
        if not os.path.exists(self.dataset_path):
            dataset = self.workspace.datasets[dataset_name]
            dataset.download(target_path=self.dataset_path, overwrite=False)


class OnlineRunInitializer(RunInitializer):
    def __init__(self, data_config: Bunch, eval_config: Bunch, run: Run):
        self.run = run
        super().__init__(data_config, eval_config)

    def run_azureml_setup(self):
        logging.info("Running in online mode...")
        self.experiment = self.run.experiment
        self.workspace = self.experiment.workspace

    def get_dataset(self):
        dataset_name = self._data_config.NAME
        # Download
        self.dataset_path = get_dataset_path(DATA_DIR_ONLINE_RUN, dataset_name)
        download_dataset(self.workspace, dataset_name, self.dataset_path)
