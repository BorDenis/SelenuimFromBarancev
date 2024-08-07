from selenium.webdriver.common.by import By


class ProductCardLocators:
    SIZE_SELECTOR = (By.XPATH, '//select[@name="options[Size]"]')
    ADD_TO_CART_BTN = (By.XPATH, '//button[@name="add_cart_product"]')
    QUANTITY_IN_CART = (By.XPATH, '//span[@class="quantity"]')
