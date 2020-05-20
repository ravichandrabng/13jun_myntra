import allure
from pathlib import Path
import os
from time import sleep


def attach_screen_shot(driver, name):
    allure.attach(driver.get_screen_shot_as_png(), name=name,
                  attachment_type=allure.attachment_type.PNG)


def delete_all_files(directory_path):
    path = Path(directory_path)
    files = path.iterdir()

    for file in files:
        if file.is_file():
            os.remove(file)

    sleep(5)

