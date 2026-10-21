from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_container = (By.CLASS_NAME, "inventory_list")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def is_loaded(self):
        return self.driver.find_element(*self.inventory_container).is_displayed()

    def add_product_by_name(self, product_name):
        add_button = (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        self.driver.find_element(*add_button).click()

    def get_cart_count(self):
        try:
            return int(self.driver.find_element(*self.cart_badge).text)
        except:
            return 0

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        self.driver.find_element(*self.logout_link).click()