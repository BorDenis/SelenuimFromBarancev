from selenium.webdriver.common.by import By


class CartLocators:
    ORDER_SUMMARY = (By.XPATH, '//tbody//td[@class="item"]')
    REMOVE_ITEM_BTN = (By.XPATH, '//li[@class="item"]//button[@name="remove_cart_item"]')
    NO_ITEMS_IN_CART = (By.XPATH, '//em[text()="There are no items in your cart."]')
    LI_SHORTCUTS = (By.XPATH, '//li[@class="shortcut"]')
