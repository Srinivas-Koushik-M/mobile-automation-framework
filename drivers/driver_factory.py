from drivers.android_driver import AndroidDriver
from drivers.ios_driver import IOSDriver

class DriverFactory:

    @staticmethod
    def get_driver(platform):

        if platform.lower() == 'android':
            return AndroidDriver.create_driver()


        elif platform.lower() == 'ios':
            return IOSDriver.create_driver()

        else:
            raise ValueError(f'Unsupported platform: {platform}')

