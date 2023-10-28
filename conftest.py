import pytest
from selenium import webdriver
import os
from selenium.webdriver.chrome import service


@pytest.fixture
def browser():
    # set up the path to operadriver executable
    webdriver_service = service.Service(os.path.abspath("driver/operadriver.exe"))
    webdriver_service.start()

    options = webdriver.ChromeOptions()
    # set up path to Opera browser executable
    options.binary_location = r"C:\Users\Starosta\AppData\Local\Programs\Opera\opera.exe"
    options.add_experimental_option('w3c', True)
    driver = webdriver.Remote(webdriver_service.service_url, options=options)

    # Set up specific site to visit
    starting_page = "https://cashback.opera.com/pl/en"
    driver.get(starting_page)
    driver.maximize_window()
    yield driver  # Provide the WebDriver instance to the test

    # Cleanup: Quit the browser after the test is done
    driver.quit()
