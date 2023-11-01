import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


def test_offer(browser):

    def element_locator(elem):
        try:
            found_elem = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable(elem)
            )
            return found_elem
        except NoSuchElementException:
            logging.info(f"{elem} was not found")

    page_elements = {
        "search_bar": (By.XPATH, "//header/div[1]/div[2]/div[4]/input[1]"),
        "shop_name": (By.TAG_NAME, "h1")
    }

    starting_page = "https://cashback.opera.com/pl/en"
    browser.get(starting_page)

    search_shop = element_locator(page_elements["search_bar"])
    ActionChains(browser).send_keys_to_element(search_shop, "allegro").send_keys(Keys.ENTER).perform()

    if element_locator(page_elements["shop_name"]).text == "Allegro":
        assert True
    else:
        assert False

