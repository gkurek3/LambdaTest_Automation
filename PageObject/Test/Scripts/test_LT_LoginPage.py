import time

from PageObject.Pages.LT_LoginPage import LTLogin
from PageObject.Pages.LT_HomePage import LTHomePage
from PageObject.Config.WebdriverSetup import webdriver_setup

driver = webdriver_setup()


class TestLTLoginPage:

    def test_click_login_link(self):
        lt_home_page_object = LTHomePage(driver)
        lt_home_page_object.lt_login_link.click()
        if driver.title == "Log in":
            print("Login page loaded successfully")
            assert driver.title == "Log in"
        else:
            print("Failed to load")

    time.sleep(5)

    def test_login_user(self):
        lt_login_page_object = LTLogin(driver)
        lt_login_page_object.get_lt_username().send_keys("gkurek3@gmail.com")
        lt_login_page_object.get_lt_password().send_keys("Lambda1234")
        lt_login_page_object.lt_login_button.click()
        time.sleep(2)
        if driver.title == "Welcome - LambdaTest":
            print("User logged in successfully")
            assert driver.title == "Welcome - LambdaTest"
        else:
            print("Failed to log the user in")
