from pathlib import Path

import allure

from utils.logger import Logger


class AllureHelper:

    logger = Logger.get_logger(__name__)

    @staticmethod
    def attach_screenshot(screenshot_path: Path | None) -> None:
        if screenshot_path is None or not screenshot_path.exists():
            AllureHelper.logger.warning(
                "Screenshot attachment skipped because file is unavailable"
            )
            return

        allure.attach.file(
            str(screenshot_path),
            name=screenshot_path.stem,
            attachment_type=allure.attachment_type.PNG
        )

    @staticmethod
    def attach_text(name: str, content: str) -> None:
        allure.attach(
            content,
            name=name,
            attachment_type=allure.attachment_type.TEXT
        )

    @staticmethod
    def attach_page_source(driver) -> None:
        if driver is None:
            return

        try:
            allure.attach(
                driver.page_source,
                name="Page Source",
                attachment_type=allure.attachment_type.XML
            )
        except Exception:
            AllureHelper.logger.exception(
                "Unable to attach page source"
            )