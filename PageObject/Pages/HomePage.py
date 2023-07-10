from selenium.webdriver.common.by import By
from PageObject.Locators.Locator_Home_Page import LTLocatorHomePage


class LTHomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_lt_login_link(self):
        return self.driver.find_element(By.XPATH, LTLocatorHomePage.login_link)

    def get_lt_signup_link(self):
        return self.driver.find_element(By.XPATH, LTLocatorHomePage.signup_link)

    def get_lt_logo(self):
        return self.driver.find_element(By.XPATH, LTLocatorHomePage.logo)
