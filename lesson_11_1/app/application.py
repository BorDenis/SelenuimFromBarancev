from selenium import webdriver
from lesson_11_1.pages.cart_page import CartPage
from lesson_11_1.pages.main_products_page import MainProductPage
from lesson_11_1.pages.product_card_page import ProductCardPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_product_page = MainProductPage(self.driver)
        self.product_card_page = ProductCardPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def quit(self):
        self.driver.quit()

    def add_first_item_to_cart_n_times(self, times=1):
        self.main_product_page.open()
        for _ in range(times):
            self.main_product_page.get_first_product()
            self.product_card_page.select_size()
            self.product_card_page.add_item_to_cart()
            self.product_card_page.is_quantity_are_changed()
            self.product_card_page.back()

    def remove_all_items_in_cart(self):
        self.cart_page.open()
        self.cart_page.remove_first_item()