import os
from functools import lru_cache

from pathlib import Path

# APPLICATION PATHS
APPLICATION_PATH = Path().cwd()
LOGS_PATH = Path(APPLICATION_PATH, "logs")

# APPLICATION DETAILS
APPLICATION_NAME = "webdis"
VERSION = "0.1-alpha"

# LOAD ENVIRONMENT SETTINGS
class Settings:
    env_var = os.environ.get('ENV_VAR')


@lru_cache()
def get_settings():
    return Settings()
