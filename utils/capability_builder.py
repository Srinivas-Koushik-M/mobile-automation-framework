from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

from config.settings import Settings


class CapabilityBuilder:

    @staticmethod
    def build():
        config = Settings.load_config()
        platform = config["platform_name"].lower()

        if platform == "android":
            return CapabilityBuilder._android_options(config)

        if platform == "ios":
            return CapabilityBuilder._ios_options(config)

        raise ValueError(f"Unsupported platform for capabilities: {platform}")

    @staticmethod
    def _android_options(config):
        options = UiAutomator2Options()

        options.platform_name = config["platform_name"]
        options.device_name = config["device_name"]
        options.automation_name = config["automation_name"]

        if config.get("platform_version"):
            options.platform_version = config["platform_version"]

        if config.get("udid"):
            options.udid = config["udid"]

        android = config.get("android", {})

        if android.get("app_package"):
            options.app_package = android["app_package"]

        if android.get("app_activity"):
            options.app_activity = android["app_activity"]

        return options

    @staticmethod
    def _ios_options(config):
        options = XCUITestOptions()

        options.platform_name = config["platform_name"]
        options.device_name = config["device_name"]
        options.automation_name = config["automation_name"]

        if config.get("platform_version"):
            options.platform_version = config["platform_version"]

        if config.get("udid"):
            options.udid = config["udid"]

        return options