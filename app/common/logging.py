import logging.config
from pathlib import Path
import time

import __init__
from app.common import config

timestr = time.strftime("%Y%m%d_%H%M%S")

path = Path(config.LOGS_PATH, f"{config.APPLICATION_NAME}_{timestr}.log")
Path(config.LOGS_PATH).mkdir(mode=0o777, parents=True, exist_ok=True)

file_handler = logging.FileHandler(path)
console_handler = logging.StreamHandler()
file_handler.setLevel(logging.INFO)
console_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))

logger = logging.getLogger(__name__)
logger.addHandler(file_handler)

logger.info(f"Version: {__init__.__version__}")

