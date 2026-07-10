from appium.webdriver.webdriver import WebDriver

from config.settings import Settings
from utils.wait_utils import WaitUtils
from selenium.common.exceptions import TimeoutException

from utils.logger import Logger

class BasePage:

    logger = Logger.get_logger(__name__)

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WaitUtils(
            driver,
            Settings.get("timeouts.explicit_wait")
        )

    def find_element(self, locator):
        return self.wait.wait_for_presence(locator)

    def find_elements(self, locator):
        return self.wait.wait_for_all_elements(locator)

    def click(self, locator):
        self.logger.info("Clicking element: %s", locator)
        self.wait.wait_for_clickable(locator).click()

    def enter_text(self, locator, text):
        self.logger.info("Entering text into element: %s", locator)
        element = self.wait.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    def clear(self, locator):
        self.logger.info("Clearing element: %s", locator)
        self.wait.wait_for_visibility(locator).clear()

    def get_text(self, locator):
        self.logger.info("Getting text from element: %s", locator)
        return self.wait.wait_for_visibility(locator).text

    def is_displayed(self, locator):
        self.logger.info("Checking if element is displayed: %s", locator)
        return self.wait.wait_for_visibility(locator).is_displayed()

    def is_enabled(self, locator):
        self.logger.info("Checking if element is enabled: %s", locator)
        return self.wait.wait_for_visibility(locator).is_enabled()

    def get_attribute(self, locator, attribute_name):
        self.logger.info("Getting attribute from element: %s", locator)
        return self.wait.wait_for_presence(locator).get_attribute(attribute_name)

    def is_selected(self, locator):
        self.logger.info("Checking if element is selected: %s", locator)
        return self.find_element(locator).is_selected()

    def wait_until_invisible(self, locator):
        self.logger.info("Waiting until element is visible: %s", locator)
        return self.wait.wait_for_invisibility(locator)

    def get_element_count(self, locator):
        self.logger.info("Getting element count: %s", locator)
        return len(self.find_elements(locator))

    def is_present(self, locator):
        try:
            self.logger.info("Checking if element is present: %s", locator)
            self.wait.wait_for_presence(locator)
            return True
        except TimeoutException:
            self.logger.info("Element is not present in the page", "exception", TimeoutException)
            return False

    def is_visible(self, locator):
        try:
            self.logger.info("Checking if element is visible: %s", locator)
            self.wait.wait_for_visibility(locator)
            return True
        except TimeoutException:
            self.logger.info("Element is not visible in the page", "exception", TimeoutException)
            return False