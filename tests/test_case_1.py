import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

def test_change_country(browser):
    def element_locator(elem):
        try:
            found_elem = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable(elem)
            )
            return found_elem
        except NoSuchElementException:
            print(f"{elem} was not found")

    def language_change(location, country):
        try:
            element_locator(page_elements[location]).click()
            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//span[text()='{country}']"))).click()
        except:
            print(f"{country} not found")

    page_elements = {
        "country_dropdown": (By.CLASS_NAME, "sdS6jS0QJPKuLdPv_jy1"),
        "language_check": (By.XPATH, "//div[contains(@class,'i_tvkjF3B2MTarDwQqDF false WxxTfgbr3cdR3yC9FzEX')]//span[contains(text(),'Deutschland')]"),
        "shop_list": (By.XPATH, "//div[@class='content']//div[@class='content']")
    }

    # Select item from menu dropdown by text
    language_change("country_dropdown", "Germany")

    language_verification = element_locator(page_elements["language_check"])
    language_check_flag = False
    if language_verification.text == "Deutschland":
        language_check_flag = True
    else:
        assert False

    content_element = element_locator(page_elements["shop_list"])
    a_tag_elements = content_element.find_elements(By.TAG_NAME, "a")
    number_of_a_elements = len(a_tag_elements)

    shops_visible_check_flag = False
    if number_of_a_elements > 10:
        shops_visible_check_flag = True
    else:
        assert False

    if language_check_flag and shops_visible_check_flag:
        language_change("country_dropdown", "Polen")
        assert True
    else:
        assert False


