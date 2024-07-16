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


def test_autorization(driver):
    driver.get('http://localhost/litecart/admin/')
    driver.find_element(By.NAME, 'username').send_keys('admin')
    driver.find_element(By.NAME, 'password').send_keys('admin')
    driver.find_element(By.NAME, 'login').click()
