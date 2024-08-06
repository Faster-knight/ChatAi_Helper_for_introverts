from config import config
from src.logger import logger
from src.timepatch import timepatch


if __name__ == '__main__':
    import os as __os

    application_path = __os.path.dirname(__file__)
    config.ParseEnv(config.env_data)
    logger.setupLogger(config.env_data)

