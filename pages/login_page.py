from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):

        self.driver = driver

    username_input = (By.XPATH, "//input[@name='username']")
    password_input = (By.XPATH, "//input[@name='password']")
    login_button = (By.XPATH, "//button[@type='submit']")

    dashboard_heading = (
        By.XPATH,
        "//h6[text()='Dashboard']"
    )

    profile_dropdown = (
        By.XPATH,
        "//span[@class='oxd-userdropdown-tab']"
    )

    logout_button = (
        By.XPATH,
        "//a[text()='Logout']"
    )

    def login(self, username, password):

        username_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.username_input)
        )

        username_field.clear()
        username_field.send_keys(username)

        password_field = self.driver.find_element(
            *self.password_input
        )

        password_field.clear()
        password_field.send_keys(password)

        self.driver.find_element(
            *self.login_button
        ).click()

    def is_login_successful(self):

        try:

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    self.dashboard_heading
                )
            )

            return True

        except:

            return False

    def logout(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.profile_dropdown
            )
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.logout_button
            )
        ).click()