import argparse
import logging.config
import pkgutil
import logging
import yaml

from sample.common.utils import load_logging_config

logger = logging.getLogger(__name__)

# def load_logging_config() -> None:
#     data = pkgutil.get_data("sample", "data/logging.yaml")
#     logging_config = yaml.safe_load(data.decode("utf-8"))
#     logging.config.dictConfig(logging_config)


def main():
    load_logging_config()

    parser = argparse.ArgumentParser(description="CSVの結果を出力")
    parser.add_argument(
        "--foo",
        nargs="+",
        required=True,
    )

    args = parser.parse_args()

    for line in args.foo:
        print(line)
    logger.info("出力しました。")


if __name__ == "__main__":
    main()
