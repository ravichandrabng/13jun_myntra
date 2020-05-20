from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotVisibleException, JavascriptException
from selenium.webdriver.support.wait import WebDriverWait
from source.utilities.properties import ReadConfig


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, ReadConfig.get_explicit_wait())
        self.driver.set_page_load_timeout(ReadConfig.get_explicit_wait())

    def find_element(self, locator, value):
        try:
            return self.driver.find_element(locator, value)
        except NoSuchElementException:
            print("Element not found")

    def click(self, web_element):
        try:
            web_element.click()
        except ElementClickInterceptedException:
            print("Unable to click on the element")

    def js_click(self, web_element):
        try:
            self.driver.exexute_script("arguments[0].click()", web_element)
        except JavascriptException:
            print("Unable to click on the element")

    def get_text(self, web_element):
        try:
            return web_element.text
        except ElementNotVisibleException:
            print("Unable to fetch the text from the browser")

    def js_get_text(self, web_element):
        try:
            self.driver.exexute_script("arguments[0].textContent", web_element)
        except JavascriptException:
            print("Unable to click on the element")


