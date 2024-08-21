import logging.config
import yaml
from pathlib import Path
import pkgutil


def load_logging_config() -> None:
    data = pkgutil.get_data("sample", "data/logging.yaml")
    logging_config = yaml.safe_load(data.decode("utf-8"))
    logging.config.dictConfig(logging_config)
