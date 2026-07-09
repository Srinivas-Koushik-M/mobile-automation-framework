from appium import webdriver
from appium.options.ios import XCUITestOptions

class IOSDriver:

    @staticmethod
    def create_driver():
        options = XCUITestOptions()

        options.platform = "ios"
        options.device_name = "iPhone 16"

        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            options=options
        )

        return driver


