import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
from os import getcwd


@pytest.fixture
def driver(request):
    wb = webdriver.Chrome()

    # options = webdriver.FirefoxOptions()
    # options.binary_location = 'C:/Program Files/Firefox Nightly/firefox.exe'
    # wb = webdriver.Firefox(options=options)

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


def test_add_new_product(driver):
    login(driver)

    catalog = (driver.find_element(By.XPATH, '//span[@class="name"][text()="Catalog"]'))
    catalog.click()
    add_new_product_btn = (driver.find_element
                           (By.XPATH, '//a[@class="button"][contains(text(), "Add New Product")]'))
    add_new_product_btn.click()
    # Product date
    p_name = f'Cool Duck{datetime.now().timestamp()}'
    p_code = 'cd001'
    p_keywords = 'black, duck, for car'
    p_description = 'Description of the product '

    # General
    status = driver.find_element(By.XPATH, '//input[@name="status"][@value=1]')
    status.click()
    name = driver.find_element(By.XPATH, '//input[@name="name[en]"]')
    name.send_keys(p_name)
    code = driver.find_element(By.XPATH, '//input[@name="code"]')
    code.send_keys(p_code)
    category_root = driver.find_element(By.XPATH, '//input[@name="categories[]"][@data-name="Root"]')
    category_root.click()
    category_rubber_ducks = driver.find_element(By.XPATH, '//input[@name="categories[]"][@data-name="Rubber Ducks"]')
    category_rubber_ducks.click()
    gender = driver.find_element(By.XPATH, '//input[@name="product_groups[]"][@value="1-3"]')
    gender.click()
    quantity = driver.find_element(By.XPATH,'//input[@name="quantity"]')
    quantity.clear()
    quantity.send_keys("5")
    sold_out_status = Select(driver.find_element(By.XPATH, '//select[@name="sold_out_status_id"]'))
    sold_out_status.select_by_visible_text('Temporary sold out')
    upload_image_file = driver.find_element(By.XPATH, '//input[@name="new_images[]"]')
    upload_image_file.send_keys(getcwd() + '/images/cool_duck.png')
    date_valid_from = driver.find_element(By.XPATH, '//input[@name="date_valid_from"]')
    date = datetime.now()
    date_valid_from.send_keys(f'{date.day}{date.month}{date.year}')

    # Information
    information_tab = driver.find_element(By.XPATH, '//div[@class="tabs"]//a[text()="Information"]')
    information_tab.click()
    keywords = driver.find_element(By.XPATH, '//input[@name="keywords"]')
    keywords.send_keys(p_keywords)
    description = driver.find_element(By.XPATH, '//div[@class="trumbowyg-editor"]')
    description.send_keys(p_description)

    # Prices
    prices_tab = driver.find_element(By.XPATH, '//div[@class="tabs"]//a[text()="Prices"]')
    prices_tab.click()
    purchase_price = driver.find_element(By.XPATH, '//input[@name="purchase_price"]')
    purchase_price.clear()
    purchase_price.send_keys('15')
    price_euro = driver.find_element(By.XPATH, '//input[@name="prices[EUR]"]')
    price_euro.send_keys("30")
    save_btn = driver.find_element(By.XPATH, '//button[@name="save"]')
    save_btn.click()

    added_product = driver.find_elements(By.XPATH, f'//tr/td/a[text()="{p_name}"]')
    assert added_product

    # Delete product
    added_product[0].click()
    delete_btn = driver.find_element(By.XPATH, '//button[@name="delete"]')
    delete_btn.click()
    driver.switch_to.alert.accept()
    assert driver.find_elements(By.XPATH,'//h1[contains(text(), "Catalog")]')
