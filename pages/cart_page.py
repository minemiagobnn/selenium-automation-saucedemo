from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.continue_shopping = (By.ID, "continue-shopping")
        self.checkout_button = (By.ID, "checkout")

    def get_number_of_items(self):
        return len(self.driver.find_elements(*self.cart_items))

    def remove_product_by_name(self, product_name):
        remove_button = (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='cart_item']//button")
        self.driver.find_element(*remove_button).click()