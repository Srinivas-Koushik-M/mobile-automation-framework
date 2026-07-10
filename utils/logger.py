import logging
from pathlib import Path

class Logger:

    LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
    LOG_FILE = LOG_DIR / "automation.log"

    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:

        cls.LOG_DIR.mkdir(parents=True, exist_ok=True)

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        if logger.handlers:
            return logger

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(cls.LOG_FILE, encoding="utf-8")
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger
    




