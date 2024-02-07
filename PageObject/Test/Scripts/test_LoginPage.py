from PageObject.Pages.LoginPage import LTLogin
from PageObject.Pages.HomePage import LTHomePage
from PageObject.Pages.HandleLoginPage import HandleLoginPage
from PageObject.Config.WebdriverSetup import WebdriverSetup
from PageObject.Config.WebdriverSetupEdge import WebdriverSetupEdge
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLTLoginPageClass:

    @classmethod
    def setup_class(cls):
        print("Setup TestClass!")
        cls.driver = WebdriverSetup().webdriver_setup()
        cls.lt_home_page_object = LTHomePage(cls.driver)
        cls.lt_login_page_object = LTLogin(cls.driver)
        cls.handle_login_page = HandleLoginPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        print("Teardown TestClass!")
        cls.driver.close()
        cls.driver.quit()
        del cls.driver

    def test_login_page_loaded(self):
        self.lt_home_page_object.get_lt_login_link().click()
        if self.driver.title == "Log in":
            print("Login page loaded successfully")
            assert self.driver.title == "Log in"
        else:
            print("Failed to load")

    def test_login_user(self):
        self.handle_login_page.handle_login()
        WebDriverWait(self.driver, 10).until(EC.title_is("Welcome - LambdaTest"))
        print("User logged in successfully")
        assert self.driver.title == "Welcome - LambdaTest"

    def test_fail_login_user(self):
        self.handle_login_page.handle_login(username="abc@gmail.com")  # wrong login credentials
        print("User failed to login")
        assert self.driver.title == "Log in"
