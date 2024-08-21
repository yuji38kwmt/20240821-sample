import logging
from sample.utils import load_logging_config

logger = logging.getLogger(__name__)

def main():
    load_logging_config()
    logger.info("hello world")

if __name__ == "__main__":
    main()
