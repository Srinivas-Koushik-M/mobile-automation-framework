from drivers.android_driver import AndroidDriver
from drivers.ios_driver import IOSDriver
from config.settings import Settings
from utils.logger import Logger


class DriverFactory:

    logger = Logger.get_logger(__name__)

    @staticmethod
    def get_driver():
        config = Settings.load_config()
        platform = config["platform_name"].lower()

        DriverFactory.logger.info(
            "Creating driver | platform=%s | environment=%s | device=%s",
            platform,
            config["env"],
            config["device"]
        )

        if platform == "android":
            return AndroidDriver.create_driver()

        if platform == "ios":
            return IOSDriver.create_driver()

        DriverFactory.logger.error("Unsupported platform: %s", platform)
        raise ValueError(f"Unsupported platform: {platform}")