import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wb = webdriver.Chrome()

    # options = webdriver.FirefoxOptions()
    # options.binary_location = 'C:/Program Files/Firefox Nightly/firefox.exe'
    # wb = webdriver.Firefox(options=options)
    # wb = webdriver.Firefox()

    # wb = webdriver.Ie()

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
    driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
    wait = WebDriverWait(driver, 10)

    add_new_country_btn = driver.find_element(
        By.XPATH, '//a[@class="button"][contains(text(), "Add New Country")]')
    add_new_country_btn.click()
    external_links = driver.find_elements(By.XPATH, '//i[contains(@class, "external-link")]')
    for i in range(len(external_links)):
        external_links = driver.find_elements(By.XPATH, '//i[contains(@class, "external-link")]')
        main_window = driver.current_window_handle
        current_handles = driver.window_handles
        external_links[i].click()
        wait.until(EC.new_window_is_opened(current_handles))
        new_window = [window for window in driver.window_handles if window != main_window][0]
        driver.switch_to.window(new_window)
        driver.close()
        driver.switch_to.window(main_window)

