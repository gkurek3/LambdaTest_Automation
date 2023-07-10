from selenium.webdriver.common.by import By
from PageObject.Locators.Locator_Login_Page import LTLocatorLoginPage


class LTLogin:

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, user_name):
        username_input = self.driver.find_element(By.XPATH, LTLocatorLoginPage.email_field)
        username_input.send_keys(user_name)

    def set_password(self, password):
        password_input = self.driver.find_element(By.XPATH, LTLocatorLoginPage.password_field)
        password_input.send_keys(password)

    def click_login_button(self):
        button = self.driver.find_element(By.XPATH, LTLocatorLoginPage.login_button)
        button.click()
