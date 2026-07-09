from appium import webdriver
from appium.options.ios import XCUITestOptions
from config.settings import Settings

class IOSDriver:

    @staticmethod
    def create_driver():
        options = XCUITestOptions()

        options.platform_name = Settings.get("ios.platform_name")
        options.device_name = Settings.get("ios.device_name")
        options.automation_name = Settings.get("ios.automation_name")


        driver = webdriver.Remote(
            command_executor=Settings.get("appium.server_url"),
            options=options
        )

        driver.implicitly_wait(Settings.get("timeout.implicitly_wait"))
        return driver


