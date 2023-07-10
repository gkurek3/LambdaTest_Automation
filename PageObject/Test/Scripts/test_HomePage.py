from PageObject.Pages.HomePage import LTHomePage
from PageObject.Config.WebdriverSetup import WebdriverSetup

driver = WebdriverSetup().webdriver_setup()


class TestLTHomepage:

    def test_home_page_title(self):
        web_page_title = "Next-Generation Mobile Apps and Cross Browser Testing Cloud | LambdaTest"
        assert driver.title == web_page_title

    def test_logo(self):
        lt_home_page_object = LTHomePage(driver)
        assert lt_home_page_object.get_lt_logo().is_displayed()

    def test_login_link(self):
        lt_home_page_object = LTHomePage(driver)
        assert lt_home_page_object.get_lt_login_link().is_displayed()

    def test_signup_link(self):
        lt_home_page_object = LTHomePage(driver)
        assert lt_home_page_object.get_lt_signup_link().is_displayed()
