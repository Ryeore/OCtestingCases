Automation tests for Opera Cashback website (https://cashback.opera.com)

Tech stack
1. Python
2. Selenium Webdriver
3. Pytest

Test Cases:

1. Changing country in header dropdown and checking visibility of shops on homepage
2. Login Form
3. Going to Shop page from search in header (exemplary URL of Shop page: https://cashback.opera.com/pl/shops/allegro)
4. Activating offer (requires being logged in)

Required packages to install. 
- pip install pytest
- pip install selenium
- pip install opencv-python
- pip install numpy
- pip install Pillow

Or just use <code>pip install -r requirements.txt</code>

Opera versions used:
- Opera One (version: 104.0.4944.33)
- [Operachromiumdriver](https://github.com/operasoftware/operachromiumdriver/releases/tag/v.118.0.5993.89)

Data sources:
- [Opera Chromedriver Setup with Selenium](https://github.com/operasoftware/operachromiumdriver/blob/master/examples/desktop_selenium_4.x.py)