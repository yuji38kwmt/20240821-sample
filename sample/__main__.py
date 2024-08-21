import argparse
import logging.config
from pathlib import Path
import pandas
import pkgutil
import logging
import yaml

logger = logging.getLogger(__name__)

def load_logging_config() -> None:
    data = pkgutil.get_data("sample", "data/logging.yaml")
    logging_config = yaml.safe_load(data.decode("utf-8"))
    logging.config.dictConfig(logging_config)
    
def print_csv(csv_path):
    df = pandas.read_csv(csv_path)
    print(df)


def main():
    load_logging_config()
    
    parser = argparse.ArgumentParser(description="CSVの結果を出力")
    parser.add_argument(
        "--csv_path",
        type=Path,
        required=True,
        help="表示するCSVファイルのパス",
    )

    args = parser.parse_args()

    print_csv(args.csv_path)
    logger.info("CSVの中身を出力しました。")

if __name__ == "__main__":
    main()
