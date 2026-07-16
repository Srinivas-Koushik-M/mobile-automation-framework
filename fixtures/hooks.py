import pytest

from utils.allure_helper import AllureHelper
from utils.logger import Logger
from utils.screenshot_utils import ScreenshotUtils


logger = Logger.get_logger(__name__)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    driver_instance = item.funcargs.get("driver")

    if report.failed:
        logger.error("Test failed | test=%s", item.name)

        screenshot_path = ScreenshotUtils.capture(
            driver_instance,
            item.name
        )

        AllureHelper.attach_screenshot(screenshot_path)
        AllureHelper.attach_page_source(driver_instance)

    elif report.passed:
        logger.info("Test passed | test=%s", item.name)

    elif report.skipped:
        logger.warning("Test skipped | test=%s", item.name)