from PageObject.Pages.HomePage import LTHomePage
from PageObject.Config.WebdriverSetup import WebdriverSetup
import unittest


class TestLTHomepage(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.driver = WebdriverSetup().webdriver_setup()
        self.lt_home_page_object = LTHomePage(self.driver)

    def test_home_page_title(self):
        web_page_title = "Next-Generation Mobile Apps and Cross Browser Testing Cloud | LambdaTest"
        assert self.driver.title == web_page_title

    def test_logo(self):
        assert self.lt_home_page_object.get_lt_logo().is_displayed()

    def test_login_link(self):
        assert self.lt_home_page_object.get_lt_login_link().is_displayed()

    def test_signup_link(self):
        assert self.lt_home_page_object.get_lt_signup_link().is_displayed()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        del self.driver


if __name__ == '__main__':
    unittest.main()
