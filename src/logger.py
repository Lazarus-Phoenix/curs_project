import logging
import os
from typing import Any


def setup_logger(name: str, file_logs: str) -> Any:
    """Настраивает работу логов"""
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(file_logs, mode="w")
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


class MockLogger:
    pass
