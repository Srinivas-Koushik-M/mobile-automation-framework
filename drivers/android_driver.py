from appium import webdriver
from appium.options.android import UiAutomator2Options

class AndroidDriver:

    @staticmethod
    def create_driver():
        options = UiAutomator2Options()

        options.platform_name = 'Android'
        options.device_name = "Android Emulator"
        options.automation_name = "UiAutomator2"

        driver = webdriver.Remote(
            command_executor='http://localhost:4723',
            options=options
        )
        return driver
    
