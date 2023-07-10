from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# def webdriver_setup():
#     chrome_options = Options()
#     chrome_options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=chrome_options)
#
#     driver.get("https://www.lambdatest.com/")
#     driver.maximize_window()
#     return driver

class WebdriverSetup:
    def __init__(self, driver):
        self.driver = driver

    def webdriver_setup(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)

        driver.get("https://www.lambdatest.com/")
        driver.maximize_window()
        return self.driver
