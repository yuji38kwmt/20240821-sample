import argparse
from pathlib import Path
import pandas


def print_csv(csv_path):
    df = pandas.read_csv(csv_path)
    print(df)


def main():
    parser = argparse.ArgumentParser(description="CSVの結果を出力")
    parser.add_argument(
        "--csv_path",
        type=Path,
        help="表示するCSVファイルのパス",
    )

    args = parser.parse_args()

    if args.csv_path is None:
        csv_path = Path(__file__).parent / "resources/default.csv"
    else:
        csv_path = args.csv_path

    print_csv(csv_path)


if __name__ == "__main__":
    main()
