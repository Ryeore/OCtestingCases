import pytest
from selenium import webdriver
from credentials import credentials
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


def test_login_form(browser):
    def element_locator(elem):
        try:
            found_elem = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(elem)
            )
            return found_elem
        except NoSuchElementException:
            print(f"{elem} was not found")

    page_elements = {
        "login_button": (By.XPATH, "//span[@class='button']"),
        "email_input": (By.XPATH, "//input[@id='email']"),
        "continue_button": (By.XPATH, "//button[@class='primaryButton']"),
        "password_input": (By.XPATH, "//input[@id='password']"),
        "username_check": (By.XPATH, "//p[@class='x1VVn_TMZQHHtH1g23tg']"),
        "popup_skip": (By.XPATH, "/html/body/main/div[7]/div/div/div[1]"),
        "successful_message": (By.XPATH, "//div[contains(@class,'wywzHy534VwpeUCBVk2p')]//div[1]//div[1]//div[1]//div[2]//input[1]")
    }

    starting_page = "https://cashback.opera.com/pl/en"
    browser.get(starting_page)

    # locate and click login
    element_locator(page_elements["login_button"]).click()

    # locate mail input field and insert value from credentials file
    mail_input = element_locator(page_elements["email_input"])
    ActionChains(browser).send_keys_to_element(mail_input, credentials.login_mail).perform()

    element_locator(page_elements["continue_button"]).click()

    # locate password input field and insert value from credentials file
    mail_input = element_locator(page_elements["password_input"])
    ActionChains(browser).send_keys_to_element(mail_input, credentials.password).perform()

    element_locator(page_elements["continue_button"]).click()
    skip = element_locator(page_elements["popup_skip"])
    if skip:
        skip.click()

    try:
        browser.get("https://cashback.opera.com/pl/profile?page=profile")
        username = element_locator(page_elements["successful_message"]).get_attribute("value")
        #if account name not changed it should be the same as the beginning of mail address
        if username is credentials.login_mail.split("@")[0] or not "":
            assert True
    except:
        assert False
