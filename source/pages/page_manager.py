from source.pages.bag_page import BagPage
from source.pages.dashboard_page import DashboardPage
from source.pages.wishlist_page import WishlistPage


def get_bag_page(driver):
    bag = None
    if driver is not None:
        bag = BagPage(driver)
    return bag


def get_dashboard_page(driver):
    dashboard = None
    if driver is not None:
        dashboard = DashboardPage(driver)
    return dashboard


def get_wishlist_page(driver):
    wishlist = None
    if driver is not None:
        wishlist = WishlistPage(driver)
    return wishlist
