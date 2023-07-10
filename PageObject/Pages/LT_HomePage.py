from selenium.webdriver.common.by import By
from PageObject.Locators import LTLocatorHomePage


class LTHomePage(object):

    def __init__(self, driver):
        self.driver = driver

        self.lt_login_link = driver.find_element(By.XPATH, LTLocatorHomePage.login_link)
        self.lt_signup_link = driver.find_element(By.XPATH, LTLocatorHomePage.signup_link)
        self.lt_logo = driver.find_element(By.XPATH, LTLocatorHomePage.logo)

    def get_lt_login_link(self):
        return self.lt_login_link

    def get_lt_signup_link(self):
        return self.lt_signup_link

    def get_lt_logo(self):
        return self.lt_logo
