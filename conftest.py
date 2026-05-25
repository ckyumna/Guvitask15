import pytest

from drivers.driver_factory import DriverFactory


@pytest.fixture
def setup():

    driver = DriverFactory.get_driver("chrome")

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    driver.implicitly_wait(10)

    print(driver.current_url)
    print(driver.title)

    yield driver

    driver.quit()