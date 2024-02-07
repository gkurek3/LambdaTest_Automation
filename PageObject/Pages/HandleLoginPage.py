from PageObject.Pages import LoginPage, HomePage
import time


class HandleLoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_page_object = LoginPage.LTLogin(driver)
        self.home_page_object = HomePage.LTHomePage(driver)

    def handle_login(self, username="gkurek3@gmail.com", password="Lambda1234"):
        self.home_page_object.get_lt_login_link().click()
        self.login_page_object.set_username(username)
        self.login_page_object.set_password(password)
        self.login_page_object.click_login_button()
