from pyjavaproperties import Properties
from source.utilities import globals
import sys


class ReadConfig:

    @staticmethod
    def get_properties():
        prop = Properties()
        prop.load(open(globals.CONFIG, mode='r'))
        return prop

    @staticmethod
    def get_browser():
        prop = ReadConfig.get_properties()
        prop_values = prop.getProperty("browser_name")
        browser_names = prop_values.split(',')
        browsers = []
        for browser in browser_names:
            browsers.append(browser)
        return browsers

    @staticmethod
    def get_url():
        prop = ReadConfig.get_properties()
        return prop.getProperty("url")

    @staticmethod
    def get_implicit_wait():
        prop = ReadConfig.get_properties()
        return int(prop.getProperty("i_wait"))

    @staticmethod
    def get_explicit_wait():
        prop = ReadConfig.get_properties()
        return int(prop.getProperty("e_wait"))

    @staticmethod
    def browser():
        prop = ReadConfig.get_properties()
        return prop.getProperty("browser_name")

    @staticmethod
    def write_to_report():
        prop = Properties()
        out = open(globals.ALLURE_RESULTS + "environment.properties", mode='w')
        prop.setProperty("Browser", ReadConfig.browser())
        prop.setProperty("URL", ReadConfig.get_url())
        prop.setProperty("Python", str(sys.version))
        window_version = str(sys.getwindowsversion())
        prop.setProperty("Platform", window_version.title())
        prop.store(out)

