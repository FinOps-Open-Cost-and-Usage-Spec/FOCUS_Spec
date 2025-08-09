import logging
import sys

def init_logger(level):
    # Create a logger instance
    logger = logging.getLogger(__name__)
    if (logger.hasHandlers()):
        logger.handlers.clear()
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))

    console_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
