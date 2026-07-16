import yaml
from pathlib import Path

from _pytest.config import Config

from config import environment
from config.environment import Environment


class Settings:

    BASE_PATH = Path(__file__).parent
    COMMON_CONFIG_PATH = BASE_PATH / "config.yml"
    ENVIRONMENTS_PATH = BASE_PATH / "environments"
    DEVICES_PATH = BASE_PATH / "devices"

    _config = None

    @classmethod
    def _load_yaml(cls, file_path):
        with open(file_path, "r") as file:
            return yaml.safe_load(file)

    @classmethod
    def load_config(cls):
        if cls._config is None:
            common_config = cls._load_yaml(cls.COMMON_CONFIG_PATH)

            env = Environment.get_env()
            device = Environment.get_device()

            environment_config = cls._load_yaml(
                cls.ENVIRONMENTS_PATH / f"{env}.yml"
            )

            device_config = cls._load_yaml(
                cls.DEVICES_PATH / f"{device}.yml"
            )

            cls._config = {
                **common_config,
                **environment_config,
                **device_config,
                "env": env,
                "device": device
            }

        return cls._config

    @classmethod
    def get(cls, key):
        config = cls.load_config()

        for item in key.split("."):
            config = config[item]

        return config
