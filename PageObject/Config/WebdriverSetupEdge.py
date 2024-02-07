from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class WebdriverSetupEdge:
    @staticmethod
    def webdriver_setup():
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

        driver.get("https://www.lambdatest.com/")
        driver.maximize_window()
        return driver
