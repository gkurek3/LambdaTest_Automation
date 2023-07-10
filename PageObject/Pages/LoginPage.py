from selenium.webdriver.common.by import By
from PageObject.Locators.Locator_Login_Page import LTLocatorLoginPage


class LTLogin:

    def __init__(self, driver):

        self.driver = driver

        self.lt_login_user_name = driver.find_element(By.XPATH, LTLocatorLoginPage.email_field)
        self.lt_login_password = driver.find_element(By.XPATH, LTLocatorLoginPage.password_field)
        self.lt_login_button = driver.find_element(By.XPATH, LTLocatorLoginPage.login_button)

    def get_lt_username(self):
        return self.lt_login_user_name

    def get_lt_password(self):
        return self.lt_login_password

    def get_lt_login_button(self):
        return self.lt_login_button
