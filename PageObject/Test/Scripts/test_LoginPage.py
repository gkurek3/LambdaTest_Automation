import time
import unittest

from PageObject.Pages.LoginPage import LTLogin
from PageObject.Pages.HomePage import LTHomePage
from PageObject.Config.WebdriverSetup import WebdriverSetup
from PageObject.Config.WebdriverSetupEdge import WebdriverSetupEdge


class TestLTLoginPage(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.driver = WebdriverSetupEdge().webdriver_setup()
        self.lt_home_page_object = LTHomePage(self.driver)
        self.lt_login_page_object = LTLogin(self.driver)

    def test_click_login_link(self):
        self.lt_home_page_object.get_lt_login_link().click()
        if self.driver.title == "Log in":
            print("Login page loaded successfully")
            assert self.driver.title == "Log in"
        else:
            print("Failed to load")

    time.sleep(3)

    def test_login_user(self):
        self.lt_home_page_object.get_lt_login_link().click()
        self.lt_login_page_object.set_username("gkurek3@gmail.com")
        self.lt_login_page_object.set_password("Lambda1234")
        self.lt_login_page_object.click_login_button()
        time.sleep(2)
        if self.driver.title == "Welcome - LambdaTest":
            print("User logged in successfully")
            assert self.driver.title == "Welcome - LambdaTest"
        else:
            print("Failed to log the user in")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        del self.driver


if __name__ == '__main__':
    unittest.main()
