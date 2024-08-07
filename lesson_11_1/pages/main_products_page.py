from selenium.webdriver.support.wait import WebDriverWait
from lesson_11_1.locators.main_products_locators import MainProductsLocators


class MainProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get('http://localhost/litecart/en/')
        return self

    def get_first_product(self):
        product_list = self.driver.find_elements(*MainProductsLocators.ALL_PRODUCTS_AT_MIDDLE)
        product_list[0].click()


