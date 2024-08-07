from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from lesson_11_1.locators.product_card_locators import ProductCardLocators

class ProductCardPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_in_cart_quantity(self):
        return int(self.driver.find_element(*ProductCardLocators.QUANTITY_IN_CART).text)

    def select_size(self, index=1):
        size_selector = self.driver.find_elements(*ProductCardLocators.SIZE_SELECTOR)
        if size_selector:
            size = Select(self.driver.find_element(*ProductCardLocators.SIZE_SELECTOR))
            size.select_by_index(index)

    def is_quantity_are_changed(self):
        quantity = self.driver.find_element(*ProductCardLocators.QUANTITY_IN_CART)
        old_quantity = int(quantity.text)
        self.wait.until(EC.text_to_be_present_in_element(ProductCardLocators.QUANTITY_IN_CART, str(old_quantity + 1)))
        new_quantity = int(self.driver.find_element(*ProductCardLocators.QUANTITY_IN_CART).text)
        assert new_quantity == old_quantity + 1

    def add_item_to_cart(self):
        add_to_cart_btn = self.driver.find_element(*ProductCardLocators.ADD_TO_CART_BTN)
        add_to_cart_btn.click()

    def back(self):
        self.driver.back()


