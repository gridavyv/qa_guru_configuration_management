from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pytest

PAGE_URL = "https://www.ebay.com/"

# the webdriver is set up before each function (because scope='function') and is automatically used by all tests (because autouse=True). 
@pytest.fixture(scope='function', autouse=True)
def browser():
    chrome_options = Options()
    chrome_options.add_experimental_option(name="detach", value=True)  # keep browser window open
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(PAGE_URL)

    # code before the yield statement is executed BEFORE the test runs
    # code after the yield statement is executed AFTER the test runs
    yield driver

    driver.close()
    print("Browser is closed.")
    driver.quit()
    print("Driver is quited.")

def test_title(browser):
    assert browser.title == "Electronics", f"Title '{browser.title} is not equals to 'Electronics'."



