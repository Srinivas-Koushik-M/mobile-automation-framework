from appium import webdriver

from config.settings import Settings
from utils.capability_builder import CapabilityBuilder


class AndroidDriver:

    @staticmethod
    def create_driver():
        config = Settings.load_config()

        driver = webdriver.Remote(
            command_executor=config["appium_server"],
            options=CapabilityBuilder.build()
        )

        driver.implicitly_wait(config["timeouts"]["implicit_wait"])
        return driver