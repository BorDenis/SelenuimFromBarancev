import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver(request):
    wb = webdriver.Chrome()

    # options = webdriver.FirefoxOptions()
    # options.binary_location = 'C:/Program Files/Firefox Nightly/firefox.exe'
    # wb = webdriver.Firefox(options=options)

    # wb = webdriver.Ie()

    request.addfinalizer(wb.quit)
    return wb


def test_check_sorting_for_countries_and_zones(driver):
    driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, 'username').send_keys('admin')
    driver.find_element(By.NAME, 'password').send_keys('admin')
    driver.find_element(By.NAME, 'login').click()
    assert driver.find_element(By.XPATH, '//*[@class="notice success"]')
    driver.implicitly_wait(2)
    all_countries_rows = driver.find_elements(By.XPATH, '//tr[@class="row"]''')
    all_countries_names = [_.find_element(By.XPATH, './/td[5]').text for _ in all_countries_rows]
    assert all_countries_names == sorted(all_countries_names)
    for country in all_countries_rows:
        zones = country.find_element(By.XPATH, './/td[6]').text
        if int(zones) > 0:
            link = country.find_element(By.XPATH, './/td[5]/a')
            ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
            driver.switch_to.window(driver.window_handles[1])
            all_zones_rows = driver.find_elements(By.XPATH, '//*[@id="table-zones"]//tr')[1:-1]
            all_zones_names = [_.find_element(By.XPATH, './/td[3]').text for _ in all_zones_rows]
            assert all_zones_names == sorted(all_zones_names)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
