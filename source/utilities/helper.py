import os
from pathlib import Path
from time import sleep

import allure
import requests


def image_broken(image_element):
    natural_width = image_element.get_attribute("naturalWidth")
    if natural_width != "0":
        return True
    else:
        return False


def check_the_links_are_broken_or_not(links):
    """ This function is used for checking the links are broken or not.
    :return Boolean, True, when the link is not broken, False, when the link is broken.
    :parameter links, this function expects list of urls.
    :exception None
            """
    flag = False
    for link in links:
        r = requests.head(link)
        if r.status_code != 404:
            flag = True
            print("link: {}, IS VALID".format(link))
        else:
            print("link: {} ISN'T VALID. Status code is: {}".format(link, r.status_code))
            flag = False
            break
    return flag


def attach_screen_shot(driver, name):
    allure.attach(driver.get_screenshot_as_png(), name=name,
                  attachment_type=allure.attachment_type.PNG)


def delete_all_files(directory_path):
    path = Path(directory_path)
    files = path.iterdir()

    for file in files:
        if file.is_file():
            os.remove(file)

    sleep(5)

