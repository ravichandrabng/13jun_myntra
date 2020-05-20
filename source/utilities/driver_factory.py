from selenium import webdriver

from source.utilities import globals
from source.utilities.properties import ReadConfig


class DriversFactory:

    def __init__(self):
        self.driver = None

    def get_web_driver(self, browser_name, url):
        if self.driver is None:
            self.driver = self.create_driver(browser_name, url)
        return self.driver

    def create_driver(self, browser_name, url):
        if browser_name == "chrome" or "ch":
            self.driver = webdriver.Chrome(executable_path=globals.CHROME_DRIVER)
        elif browser_name == "firefox" or "ff":
            self.driver = webdriver.Firefox(executable_path=globals.FIREFOX_DRIVER)
        elif browser_name == "internet explorer" or "ie":
            self.driver = webdriver.ie(executable_path=globals.IE_DRIVER)
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.implicitly_wait(ReadConfig.get_implicit_wait())
        return self.driver
