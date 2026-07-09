from drivers.android_driver import AndroidDriver
from drivers.ios_driver import IOSDriver
from config.settings import Settings


class DriverFactory:

    @staticmethod
    def get_driver():
        config = Settings.load_config()
        platform = config["platform_name"].lower()

        if platform == "android":
            return AndroidDriver.create_driver()

        if platform == "ios":
            return IOSDriver.create_driver()

        raise ValueError(f"Unsupported platform: {platform}")