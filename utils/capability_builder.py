from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from pathlib import Path
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

        app_path = config.get("app", {}).get("path")

        if app_path:
            absolute_app_path = (
                    Path(__file__).resolve().parent.parent / app_path
            ).resolve()

            if not absolute_app_path.exists():
                raise FileNotFoundError(
                    f"APK not found: {absolute_app_path}"
                )

            options.app = str(absolute_app_path)

        android_config = config.get("android", {})

        if android_config.get("app_package"):
            options.app_package = android_config["app_package"]

        if android_config.get("app_activity"):
            options.app_activity = android_config["app_activity"]

        if android_config.get("app_wait_activity"):
            options.app_wait_activity = android_config["app_wait_activity"]

        options.app_wait_duration = 60000
        options.auto_grant_permissions = True
        options.new_command_timeout = 300

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