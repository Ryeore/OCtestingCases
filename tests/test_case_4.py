import numpy as np
import pytest
from selenium import webdriver
from credentials import credentials
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import cv2
from PIL import ImageGrab


def template_match(image, template):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    threshold = 0.8  # Adjust the threshold as needed
    if max_val >= threshold:
        return max_loc

    return None


def match_location(temp):
    template = cv2.imread(f'templates/{temp}.png')
    found = True
    time.sleep(1)
    while found:
        screenshot = np.array(ImageGrab.grab())
        location = template_match(screenshot, template)
        if location is not None:
            found = False
    return True


def test_cashback(browser):

    def element_locator(elem):
        try:
            found_elem = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable(elem)
            )
            return found_elem
        except NoSuchElementException:
            print(f"{elem} was not found")

    page_elements = {
        "cashback_option": (By.XPATH, "//a[@id='675bf072-3ae7-42f5-ad5a-1adcad65b508']"),
        "start_cashback": (By.XPATH, "//span[@class='button']"),
        "cashback_confirmation": (By.ID, "dynamic-title"),
    }

    element_locator(page_elements["start_cashback"]).click()
    if match_location("cashback_confirmed"):
        assert True
    else:
        assert False

