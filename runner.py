import os
from datetime import datetime
from time import sleep

import pytest

from source.utilities import globals, helper


class ReportPlugin:

    def pytest_sessionfinish(self):
        globals.ALLURE_REPORT = globals.ALLURE_REPORT + datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        os.popen("allure generate " + globals.ALLURE_RESULTS + " --output " + globals.ALLURE_REPORT)


'''file_path = "./requirements.txt"
abs_path = os.path.abspath(file_path)
command = "pip install -r " + abs_path
os.system(command)

sleep(15)
helper.delete_all_files(globals.ALLURE_RESULTS)'''

args = ['-n', '2', '--alluredir', globals.ALLURE_RESULTS]
pytest.main(args, plugins=[ReportPlugin()])
