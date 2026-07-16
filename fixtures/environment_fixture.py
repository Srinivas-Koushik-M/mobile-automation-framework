import os

import pytest

from utils.logger import Logger


logger = Logger.get_logger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        choices=["qa", "uat", "prod"],
        help="Execution environment"
    )

    parser.addoption(
        "--device",
        action="store",
        default="android_emulator",
        choices=[
            "android_emulator",
            "android_real",
            "ios_simulator",
            "ios_real"
        ],
        help="Execution device"
    )


@pytest.fixture(scope="session", autouse=True)
def configure_execution(request):
    env = request.config.getoption("--env")
    device = request.config.getoption("--device")

    os.environ["ENV"] = env
    os.environ["DEVICE"] = device

    logger.info(
        "Execution configured | environment=%s | device=%s",
        env,
        device
    )