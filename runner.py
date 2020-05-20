from datetime import datetime
from time import sleep
import pytest
import os
from source.utilities import globals, helper


class ReportPlugin:

    def pytest_sessionfinish(self):
        globals.ALLURE_REPORT = globals.ALLURE_REPORT + datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        os.popen("allure generate "+globals.ALLURE_RESULTS+ " --output "+globals.ALLURE_REPORT)

        sleep(15)
        helper.delete_all_files(globals.ALLURE_RESULTS)


args = ['--alluredir', globals.ALLURE_RESULTS]
pytest.main(args, plugins=[ReportPlugin()])


