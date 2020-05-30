from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, JavascriptException, \
    TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from source.utilities.properties import ReadConfig
from source.utilities.webdriver_wrapper import Actions


class BasePage:
    """ This class is a super class for all the page classes,
    initialises web-driver for the pages, and contains all the common utilities functions required by all the page classes.
     """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, ReadConfig.get_explicit_wait())
        self.driver.set_page_load_timeout(ReadConfig.get_explicit_wait())
        self.action = Actions(self.driver)
        self.flag = False

    def find_element(self, locator, value):
        """ This function is used for finding an element on the web page and return element
        :parameter locator
        :parameter value
        :return first matching element
        :except no such element"""
        try:
            return self.driver.find_element(locator, value)
        except NoSuchElementException as exp:
            raise NoSuchElementException(
                "{}: No such element, locator type: {}, locator value: {} ".format(exp, locator, value))

    def find_elements(self, locator, value):
        """ This function is used for finding all the matching elements on the web page and return list of elements
        :parameter locator
        :parameter value
        :returns list of elements
        :raise no such element, when no matching element found"""
        elements = self.driver.find_elements(locator, value)
        if len(elements) <= 0:
            raise NoSuchElementException("Exception: elements not found, locator type: %d, locator value: %d ", locator,
                                         value)
        return elements

    def click(self, element):
        """ This function is used to wait till the element become visible/enable in the UI. and once the
         element is visible/enabled, clicks on the element.
         :parameter element
         :return None
         :except ElementClickInterceptedException, ElementNotVisibleException, Exception"""
        try:
            self.wait_for_element_to_click(element).click()
        except Exception as exp:
            raise Exception("{}, Unable to click on the element. ".format(exp))

    def send_keys(self, element, text_to_type):
        """ This function is used to wait for the element to be visible. And
        type the text in the text box.
        :parameter element
        :parameter text_to_type
        :return None
        :except exception"""
        try:
            self.wait_for_element_to_visible(element)
            element.send_keys(text_to_type)
        except Exception as exp:
            print("Unable to type the text in the text box: ", exp)
            raise Exception("{}, Unable to type the text in the text box. ".format(exp))

    def js_click(self, element):
        """ This function is used to wait till the element become visible/enable in the UI. and once the
                 element is visible/enabled, clicks on the element using JavaScript.
        :parameter element
        :return None
        :except JavascriptException"""
        self.wait_for_element_to_click(element)
        self.driver.exexute_script("arguments[0].click()", element)
        raise JavascriptException("Unable to click on the element using Java Script Click() function".format())

    def get_text(self, element):
        """ This function is used to wait for the element to be visible, to get the text of an element.
        :param element
        :return text of an element, if visible else return empty string
        :except Element not visible exception """
        text_ = ""
        try:
            self.wait_for_element_to_visible(element)
            text_ = element.text
            return text_
        except ElementNotVisibleException as exp:
            print("Unable to fetch the text from the browser", exp)
            return text_

    def js_get_text(self, element):
        """ This function is used to wait for an element to be visible to get the text of an element using JavaScript.
        :parameter element
        :return text of an element
        :except JavascriptException"""
        value = ""
        try:
            self.wait_for_element_to_visible(element)
            value = self.driver.exexute_script("arguments[0].textContent", element)
        except JavascriptException as exp:
            print("Unable to get the text of an element", exp)
        return value

    def wait_for_element_to_visible(self, element):
        """ This function is used to wait for an element, until the element visible on the UI within the specified time.
        :parameter element
        :return None
        :except Time out exception"""
        self.flag = False
        try:
            self.wait.until(ec.visibility_of(element))
            self.flag = True
        except TimeoutException as exp:
            print("Expected element is not visible: ", exp)
            self.flag = False
        return self.flag

    def wait_for_element_to_click(self, element):
        """ This function is used to wait for an element, until the element visible, enables on the UI with in the specified time.
        :parameter element
        :return element if an element become visible and enabled, else return none
        :except time out exception"""
        try:
            self.wait_for_element_to_visible(element)
            if element.is_enabled():
                return element
        except TimeoutException as exp:
            print("Expected element is not displayed and disabled: ", exp)

    def verify_title(self, title_of_the_page):
        """ This function is used for verifying the title of the page.
        :parameter title_of_the_page
        :return True, if the page title matches with the expected title else False
        :except time out exception"""
        try:
            return self.wait.until(ec.title_contains(title_of_the_page))
        except TimeoutException as exp:
            print("Expected element is not displayed and disabled: ", exp)
            return False

    def verify_text_of_an_element(self, element, text_to_verify):
        """ This function is used for verifying the text of an element.
        :parameter element
        :parameter text_to_verify
        :return True, if the expected text present in the element, else False
        :except expeption"""
        flag = False
        text_ = ""
        try:
            self.wait_for_element_to_visible(element)
            text_ = element.text
            if text_to_verify in text_:
                flag = True
            return flag
        except Exception as exp:
            print("Expected text '%s' is not matching with actual text '%s' ", text_to_verify, text_, exp)
