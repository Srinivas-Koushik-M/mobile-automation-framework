from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains


class GestureUtils:

    def __init__(self, driver):
        self.driver = driver

    def swipe_up(self, duration=800):
        size = self.driver.get_window_size()

        start_x = size["width"] // 2
        start_y = int(size["height"] * 0.8)

        end_x = size["width"] // 2
        end_y = int(size["height"] * 0.2)

        self.driver.swipe(
            start_x,
            start_y,
            end_x,
            end_y,
            duration
        )

    def swipe_down(self, duration=800):
        size = self.driver.get_window_size()

        start_x = size["width"] // 2
        start_y = int(size["height"] * 0.2)

        end_x = size["width"] // 2
        end_y = int(size["height"] * 0.8)

        self.driver.swipe(
            start_x,
            start_y,
            end_x,
            end_y,
            duration
        )


    def swipe_left(self, duration=800):
        size = self.driver.get_window_size()

        start_x = int(size["width"] * 0.8)
        start_y = size["height"] // 2

        end_x = int(size["width"] * 0.2)
        end_y = int(size["height"] // 2 )

        self.driver.swipe(
            start_x,
            start_y,
            end_x,
            end_y,
            duration
        )

    def swipe_right(self, duration=800):
        size = self.driver.get_window_size()

        start_x = int(size["width"] * 0.2)
        start_y = size["height"] // 2

        end_x = int(size["width"] * 0.8)
        end_y = int(size["height"] // 2)

        self.driver.swipe(
            start_x,
            start_y,
            end_x,
            end_y
        )

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
            return True
        except Exception:
            return False


    def long_press(self, locator, duration=2):
        element = self.driver.find_element(*locator)

        actions = ActionChains(self.driver)
        actions.click_and_hold(element)
        actions.pause(duration)
        actions.release()
        actions.perform()

    def double_tap(self, locator):
        element = self.driver.find_element(*locator)

        actions = ActionChains(self.driver)
        actions.double_click(element)
        actions.perform()


    def drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target)
        actions.perform()


    def tap(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def scroll_to_text(self, text):
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().text("{text}"))'
        )

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )
        return element

