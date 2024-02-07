from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class WebdriverSetup:
    @staticmethod
    def webdriver_setup():
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver.implicitly_wait(10)
        driver.get("https://www.lambdatest.com/")
        driver.maximize_window()
        return driver
