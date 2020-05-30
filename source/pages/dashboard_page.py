"""
@description: Class represents the Bag web page.
@author: Pramod KS
"""
import allure
from selenium.webdriver.common.by import By

from source.pages.base_page import BasePage
from source.utilities import helper


class DashboardPage(BasePage):
    # Functions which returns the web elements
    def __menu_bars(self):
        return self.find_elements(By.CSS_SELECTOR, "div[class='desktop-navContent']>div[class='desktop-navLink']>a")

    def __links_under_menu_bars(self, menu_name):
        return self.find_elements(By.CSS_SELECTOR,
                                  "a[data-group='" + menu_name + "']+div div[class='desktop-categoryContainer']>li>ul>li>a")

    def __search_box(self):
        return self.find_element(By.CSS_SELECTOR, "input[placeholder='Search for products, brands and more']")

    def __search_submit_button(self):
        return self.find_element(By.CSS_SELECTOR, "a[class='desktop-submit']")

    def __company_logo(self):
        return self.find_element(By.CSS_SELECTOR, "a[class='myntraweb-sprite desktop-logo sprites-headerLogo']")

    # Functions to perform the actions on the web elements

    @allure.step
    def company_logo_broken(self):
        return helper.image_broken(self.__company_logo())

    @allure.step
    def company_logo_displayed(self):
        return self.wait_for_element_to_visible(self.__company_logo())

    @allure.step
    def enter_product_name_in_search_box(self, product_name):
        self.send_keys(self.__search_box(), product_name)
        self.click(self.__search_submit_button())

    @allure.step
    def verify_the_links_under_men_bar_not_broken(self):
        menus = self.__menu_bars()
        l = ""
        for menu in menus:
            self.action.move_to_element(menu)
            menu_name = menu.get_attribute("data-group")
            links = self.__links_under_menu_bars(menu_name)
            urls = []
            for link in links:
                href = link.get_attribute("href")

                if "https" in href:
                    l = href
                else:
                    l = "https://www.myntra.com/" + href

                urls.append(l)

            if helper.check_the_links_are_broken_or_not(urls):
                self.flag = True
            else:
                self.flag = False
                break
        return self.flag
