from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.settings import Settings

class AndroidDriver:

    @staticmethod
    def create_driver():
        config = Settings.load_config()

        options = UiAutomator2Options()
        options.platform = config["platform_name"]
        options.device_name = config["device_name"]
        options.automation_name = config["automation_name"]

        if config.get("platform_version"):
            options.platform_version = config["platform_version"]

        if config.get("udid"):
            options.udid = config["udid"]

        if config.get("android", {}).get("app_package"):
            options.app_package = config["android"]["app_package"]

        if config.get("android", {}).get("app_activity"):
            options.app_activity = config["android"]["app_activity"]

        options.platform_name = Settings.get("android.platform.name")
        options.device_name = Settings.get("android.device.name")
        options.automation_name = Settings.get("android.automation_name")

        driver = webdriver.Remote(
            command_executor=config["appium_server"],
            options=options
        )

        driver.implicitly_wait(config["timeouts"]["implicit_wait"])

        return driver


