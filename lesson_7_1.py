import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    # wb = webdriver.Chrome()

    # options = webdriver.FirefoxOptions()
    # options.binary_location = 'C:/Program Files/Firefox Nightly/firefox.exe'
    # wb = webdriver.Firefox(options=options)
    # wb = webdriver.Firefox()

    wb = webdriver.Ie()

    request.addfinalizer(wb.quit)
    return wb


def test_add_new_product(driver):
    driver.implicitly_wait(2)
    driver.get('http://localhost/litecart/en/')
    wait = WebDriverWait(driver, 3)

    times_repeat = 3
    for i in range(1, times_repeat):
        products = driver.find_elements(By.XPATH, '//li[contains(@class, "product")]')
        products[0].click()
        size_locator = '//select[@name="options[Size]"]'
        if driver.find_elements(By.XPATH, size_locator):
            size = Select(driver.find_element(By.XPATH, size_locator))
            size.select_by_index(1)
        add_to_cart = driver.find_element(By.XPATH, '//button[@name="add_cart_product"]')
        add_to_cart.click()
        wait.until(EC.text_to_be_present_in_element((By.XPATH, '//span[@class="quantity"]'), str(i)))
        # assert driver.find_element(By.XPATH, f'//span[@class="quantity"][text()={i}]')
        driver.back()
    cart_checkout = driver.find_element(By.XPATH, '//div[@id="cart"]/a[@class="link"]')
    cart_checkout.click()
    order_summary = driver.find_elements(By.XPATH, '//tbody//td[@class="item"]')

    for _ in range(len(order_summary)):
        remove_btn = driver.find_element(By.XPATH, '//li[@class="item"]//button[@name="remove_cart_item"]')
        removed_product_name = remove_btn.find_element(By.XPATH, '../..//a').text
        remove_btn.click()
        assert not driver.find_elements(By.XPATH, f'//tbody//td[@class="{removed_product_name}"]')

    assert driver.find_elements(By.XPATH, '//em[text()="There are no items in your cart."]')
