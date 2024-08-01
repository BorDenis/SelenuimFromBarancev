import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime


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


def test_new_user_registration(driver):
    driver.implicitly_wait(2)
    driver.get('http://localhost/litecart/en/')

    # User data
    u_first_name = 'Ivan'
    u_last_name = 'Sidorov'
    u_address_1 = '1600 Amphitheatre Parkway'
    u_postcode = '94043'
    u_city = 'Mountain View'
    u_country = 'United States'
    u_state = 'Utah'
    u_email = f'ivan_sid_{datetime.now().timestamp()}@gmail.com'
    u_phone = '16019521325'
    u_password = 'IvSid94043'

    # Registration
    login_box = driver.find_element(By.XPATH, '//div[@id="box-account-login"]')
    registration_link = login_box.find_element(By.XPATH,'.//tr[5]//a')
    registration_link.click()
    create_account_box = driver.find_element(By.XPATH, '//div[@id="create-account"]')
    first_name = create_account_box.find_element(By.XPATH, './/input[@name="firstname"]')
    first_name.send_keys(u_first_name)
    last_name = create_account_box.find_element(By.XPATH, './/input[@name="lastname"]')
    last_name.send_keys(u_last_name)
    address_1 = create_account_box.find_element(By.XPATH, './/input[@name="address1"]')
    address_1.send_keys(u_address_1)
    postcode = create_account_box.find_element(By.XPATH, './/input[@name="postcode"]')
    postcode.send_keys(u_postcode)
    city = create_account_box.find_element(By.XPATH, './/input[@name="city"]')
    city.send_keys(u_city)
    country = create_account_box.find_element(By.XPATH, './/span[@class="select2-selection__arrow"]')
    country.click()
    country_dropdown = create_account_box.find_element(
        By.XPATH, f'//ul[@class="select2-results__options"]/li[text()="{u_country}"]')
    country_dropdown.click()
    state = Select(create_account_box.find_element(By.XPATH, './/select[@name="zone_code"]'))
    state.select_by_visible_text(u_state)
    email = create_account_box.find_element(By.XPATH, './/input[@name="email"]')
    email.send_keys(u_email)
    phone = create_account_box.find_element(By.XPATH, './/input[@name="phone"]')
    phone.send_keys(u_phone)
    password = create_account_box.find_element(By.XPATH, './/input[@name="password"]')
    password.send_keys(u_password)
    confirmed_password = create_account_box.find_element(By.XPATH, './/input[@name="confirmed_password"]')
    confirmed_password.send_keys(u_password)
    create_account_btn = create_account_box.find_element(By.XPATH, './/button[@name="create_account"]')
    create_account_btn.click()

    # Logout
    logout_link = driver.find_element(By.XPATH, '//div[@id="box-account"]//a[text()="Logout"]')
    logout_link.click()

    # Login
    login_email = driver.find_element(By.XPATH, '//input[@name="email"]')
    login_email.send_keys(u_email)
    login_password = driver.find_element(By.XPATH, '//input[@name="password"]')
    login_password.send_keys(u_password)
    login_btn = driver.find_element(By.XPATH, '//button[@name="login"]')
    login_btn.click()

    # Logout
    logout_link = driver.find_element(By.XPATH, '//div[@id="box-account"]//a[text()="Logout"]')
    logout_link.click()
