import logging
import yaml
from pathlib import Path


def load_logging_config() -> None:
    logging_config_file = Path(__file__).parent / "data/logging.yaml"
    print(f"{logging_config_file=}")
    logging_config = yaml.safe_load(logging_config_file.open())
    logging.config.dictConfig(logging_config)
