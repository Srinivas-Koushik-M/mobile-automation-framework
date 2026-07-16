import pytest

from drivers.driver_factory import DriverFactory
from utils.logger import Logger


logger = Logger.get_logger(__name__)


@pytest.fixture(scope="function")
def driver(configure_execution):
    logger.info("Creating Appium driver")

    mobile_driver = DriverFactory.get_driver()

    try:
        yield mobile_driver
    finally:
        logger.info("Closing Appium driver")

        if mobile_driver:
            mobile_driver.quit()