import os


class Environment:

    DEFAULT_ENV = "qa"
    DEFAULT_DEVICE=  "android_emulator"


    SUPPORTED_ENVS = ["qa", "uat", "prod"]
    SUPPORTED_DEVICES = [
        "android_emulator",
        "android_real",
        "ios_simulator",
        "ios_real"
    ]




    @classmethod
    def get_env(cls):
        env = os.getenv("ENV", cls.DEFAULT_ENV).lower()

        if env not in cls.SUPPORTED_ENVS:
            raise ValueError(
                f"Invalid environment: {env}. Supported environments: {cls.SUPPORTED_ENVS}"
            )

        return env

    @classmethod
    def get_device(cls):
        device = os.getenv("DEVICE", cls.DEFAULT_DEVICE).lower()

        if device not in cls.SUPPORTED_DEVICES:
            raise ValueError(
                f"Invalid device: {device}. Supported devices: {cls.SUPPORTED_DEVICES}"
            )

        return device