import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.set_capability("goog:loggingPrefs", {'browser': 'ALL'})
    wb = webdriver.Chrome(options=options)

    # options = webdriver.FirefoxOptions()
    # options.binary_location = 'C:/Program Files/Firefox Nightly/firefox.exe'
    # wb = EventFiringWebDriver(webdriver.Firefox(options=options), MyListener())

    # wb = EventFiringWebDriver(webdriver.IE(), MyListener())

    request.addfinalizer(wb.quit)
    return wb


def login(driver):
    driver.get('http://localhost/litecart/admin')
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, 'username').send_keys('admin')
    driver.find_element(By.NAME, 'password').send_keys('admin')
    driver.find_element(By.NAME, 'login').click()
    assert driver.find_element(By.XPATH, '//*[@class="notice success"]')
    driver.implicitly_wait(2)


def test_check_that_links_is_opening_in_new_tabs(driver):
    login(driver)
    driver.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')
    edit_btn_locator = '//tr[@class="row"]/td/a[contains(@href, "product")][@title="Edit"]'
    edit_product_btns = driver.find_elements(By.XPATH, edit_btn_locator)
    for i in range(len(edit_product_btns)):
        edit_product_btns = driver.find_elements(By.XPATH, edit_btn_locator)
        edit_product_btns[i].click()
        assert driver.get_log('browser')
        driver.back()



