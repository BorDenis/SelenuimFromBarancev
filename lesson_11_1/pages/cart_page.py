from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_11_1.locators.cart_locators import CartLocators


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get('http://localhost/litecart/en/checkout')

    def get_order_summary_len(self):
        return len(self.driver.find_elements(*CartLocators.ORDER_SUMMARY))

    def remove_first_item(self):
        wait = WebDriverWait(self.driver, 2)
        shortcuts = self.driver.find_elements(*CartLocators.LI_SHORTCUTS)
        if shortcuts:
            shortcuts[0].click()
        remove_btn = self.driver.find_element(*CartLocators.REMOVE_ITEM_BTN)
        removed_product_name = remove_btn.find_element(By.XPATH, '../..//a').text
        remove_btn.click()
        assert not self.driver.find_elements(By.XPATH, f'//tbody//td[@class="{removed_product_name}"]')
        wait.until(EC.staleness_of(remove_btn))

    def is_cart_are_empty(self):
        try:
            self.driver.find_element(*CartLocators.NO_ITEMS_IN_CART)
        except NoSuchElementException:
            return False
        return True
