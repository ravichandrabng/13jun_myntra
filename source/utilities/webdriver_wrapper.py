import allure
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from source.utilities.properties import ReadConfig


@allure.step
def switch_to_child_window(driver):
    """ This function is used to change the control from one window to another window.
    :author Pramod KS
    :parameter web-driver
    :return none
    :except No such window exception"""
    child_window = None
    parent_window = driver.current_window_handle
    window_ids = driver.window_handles
    try:
        for window_id in window_ids:
            if window_id != parent_window:
                child_window = window_id
                break

        driver.switch_to.window(child_window)
    except NoSuchWindowException as exp:
        print("Exception: {} Unable to change the focus to child Window/Tab.".format(exp))


class Actions:
    """ This class is used for handling all the mouse related operations.
    :author: Pramod KS"""

    def __init__(self, driver):
        self.action = ActionChains(driver)

    def move_to_element(self, element):
        self.action.move_to_element(element).perform()

    def right_click(self, element):
        self.action.context_click(element).perform()

    def drag_and_drop(self, source, target):
        self.action.drag_and_drop(source, target).perform()


class DropDrown:

    def __init__(self, element):
        self.select = Select(element)

    def select_by_index_num(self, index):
        self.select.select_by_index(index)

    def select_by_text(self, visible_text):
        self.select.select_by_visible_text(visible_text)

    def select_by_attribute_value(self, attribute_value):
        self.select.select_by_value(attribute_value)

    def get_all_options_from_drop_down(self):
        return self.select.options


class AlertHandler:

    def __int__(self, driver):
        self.wait = WebDriverWait(driver, ReadConfig.get_explicit_wait())
        self.alert = self.wait.until(ec.alert_is_present())

    def accept_alert(self):
        try:
            self.alert.accept
        except Exception as exp:
            raise Exception("{}".format(exp))

    def dismiss_alert(self):
        try:
            self.alert.dismiss
        except Exception as exp:
            raise Exception("{}".format(exp))

    def get_alert_text(self):
        try:
            self.alert.text
        except Exception as exp:
            raise Exception("{}".format(exp))
