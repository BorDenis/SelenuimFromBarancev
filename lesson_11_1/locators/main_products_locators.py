from selenium.webdriver.common.by import By


class MainProductsLocators:
    ALL_PRODUCTS_AT_MIDDLE = (By.XPATH, '//li[contains(@class, "product")]')
    CART_CHECKOUT_LINK = (By.XPATH, '//div[@id="cart"]/a[@class="link"]')