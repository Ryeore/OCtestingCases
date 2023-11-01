import logging
from selenium.webdriver import Keys
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
        "search_bar": (By.XPATH, "//input[@placeholder='Search for a shop...']")
    }

    search_shop = element_locator(page_elements["search_bar"])
    ActionChains(browser).send_keys_to_element(search_shop, "allegro").send_keys(Keys.ENTER).perform()

    if browser.find_element(By.XPATH, "//h1[@class='uFOHmfzloPqKBpMp52yB stats-button-login']").text == "Allegro":
        assert True
    else:
        assert False

