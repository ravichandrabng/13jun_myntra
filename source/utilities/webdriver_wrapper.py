import allure
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver import ActionChains

"""
Author: Pramod KS
Description: For changing the focus to the Child Tab/Window
Arguments: Web driver
Return type: None
Exceptions: throws NoSuchWindowException 
"""
@allure.step
def switch_to_child_window(driver):
    child_window = None
    parent_window = driver.current_window_handle
    window_ids = driver.window_handles
    try:
        for window_id in window_ids:
            if window_id != parent_window:
                child_window = window_id
                break

        driver.switch_to.window(child_window)
    except NoSuchWindowException:
        print("Unable to change the focus to child Window/Tab.")


class Actions:

    def __init__(self, driver):
        self.action = ActionChains(driver)

    def move_to_element(self, element):
        self.action.move_to_element(element).perform()

    def right_click(self, element):
        self.action.context_click(element).perform()

    def drag_and_drop(self, source, target):
        self.action.drag_and_drop(source, target).perform()
