from datetime import datetime
from pathlib import Path

from utils.logger import Logger


class ScreenshotUtils:

    SCREENSHOT_DIR = (
        Path(__file__).resolve().parent.parent
        / "screenshots"
        / "failed"
    )

    logger = Logger.get_logger(__name__)

    @classmethod
    def capture(cls, driver, test_name: str) -> Path | None:
        if driver is None:
            cls.logger.warning(
                "Screenshot skipped because driver is unavailable | test=%s",
                test_name
            )
            return None

        cls.SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

        safe_test_name = "".join(
            character if character.isalnum() or character in "-_"
            else "_"
            for character in test_name
        )

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        screenshot_path = (
            cls.SCREENSHOT_DIR
            / f"{safe_test_name}_{timestamp}.png"
        )

        try:
            captured = driver.save_screenshot(str(screenshot_path))

            if not captured:
                cls.logger.error(
                    "Driver returned False while capturing screenshot | test=%s",
                    test_name
                )
                return None

            cls.logger.info(
                "Screenshot captured | path=%s",
                screenshot_path
            )
            return screenshot_path

        except Exception:
            cls.logger.exception(
                "Screenshot capture failed | test=%s",
                test_name
            )
            return None