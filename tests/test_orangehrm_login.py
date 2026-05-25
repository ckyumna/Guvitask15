from pages.login_page import LoginPage
from utilities.excel_reader import ExcelReader


def test_login(setup):

    driver = setup

    login_page = LoginPage(driver)

    data = ExcelReader.get_multiple_test_data("Sheet1")

    for index, row_data in enumerate(data, start=2):

        driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

        username = row_data["Username"]

        password = row_data["Password"]

        login_page.login(username, password)

        if login_page.is_login_successful():

            ExcelReader.write_result(
                "Sheet1",
                index,
                "Pass"
            )

            login_page.logout()

        else:

            ExcelReader.write_result(
                "Sheet1",
                index,
                "Fail"
            )