import sys
import logging
from logging.handlers import RotatingFileHandler


class Logger:
    @staticmethod
    def getLogger():
        # Create a logger for the module
        logger = logging.getLogger(__name__)
        # Set the log level to DEBUG
        logger.setLevel(logging.DEBUG)

        # Create a formatter with ISO-8601 timestamp
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%dT%H:%M:%S%z"
        )
        # Create a rotating file handler with 10 MB size limit and 10 backup files
        file_handler = logging.handlers.RotatingFileHandler(
            filename=f"/tmp/{__name__}.log", maxBytes=10 * 1024 * 1024, backupCount=10
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Create and configure a stream handler (console output)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        return logger


# Obtain the configured logger
logger = Logger.getLogger()