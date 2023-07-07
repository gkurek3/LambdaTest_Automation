from selenium.webdriver.common.by import By
from PageObject.Locators import LTLocator


class LTLogin(object):

    def __init__(self, driver):

        self.driver = driver

        self.lt_login_user_name = driver.find_element(By.XPATH, LTLocator.email_field)
        self.lt_login_password = driver.find_element(By.XPATH, LTLocator.password_field)
        self.lt_login_button = driver.find_element(By.XPATH, LTLocator.login_button)

    def get_lt_username(self):
        return self.lt_login_user_name

    def get_lt_password(self):
        return self.lt_login_password

    def get_lt_login_button(self):
        return self.lt_login_button
