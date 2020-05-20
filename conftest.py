import os
import pytest
from source.utilities import helper
from source.utilities.driver_factory import DriversFactory
from source.utilities.properties import ReadConfig


@pytest.fixture(scope="session", autouse=True)
def add_environment_details_to_allure_report():
    file_path = "./requirements.txt"
    abs_path = os.path.abspath(file_path)
    command = "pip install -r " + abs_path
    os.system(command)
    yield
    ReadConfig.write_to_report()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    print(call)
    rep = outcome.get_result()
    setattr(item, "rep_"+rep.when, rep)


@pytest.fixture(scope="function", params=ReadConfig.get_browser(), autouse=True)
def set_up(request):
    browser_name = request.param
    url = ReadConfig.get_url()
    factory = DriversFactory()
    driver = factory.get_web_driver(browser_name, url)
    if driver is not None:
        request.node.driver = driver
    yield
    if request.node.rep_call.failed:
        helper.attach_screen_shot(driver, request.function.__name__)
    driver.quit()
