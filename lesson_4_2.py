import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    wb = webdriver.Chrome()

    # options = webdriver.FirefoxOptions()
    # options.binary_location = 'C:/Program Files/Firefox Nightly/firefox.exe'
    # wb = webdriver.Firefox(options=options)

    # wb = webdriver.Ie()

    request.addfinalizer(wb.quit)
    return wb


def test_check_stickers(driver):
    driver.get('http://localhost/litecart/en/')
    driver.implicitly_wait(2)
    all_products = driver.find_elements(By.XPATH, "//li[contains(@class, 'product')]")
    for product in all_products:
        stickers = product.find_elements(By.XPATH, ".//div[contains(@class,'sticker')]")
        assert len(stickers) == 1