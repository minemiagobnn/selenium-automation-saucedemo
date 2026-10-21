import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_add_product_to_cart(driver):
    """Test case 4: Thêm 1 sản phẩm vào giỏ hàng"""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_product_by_name("Sauce Labs Backpack")
    assert inventory_page.get_cart_count() == 1

def test_add_multiple_products(driver):
    """Test case 5: Thêm nhiều sản phẩm vào giỏ hàng"""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_product_by_name("Sauce Labs Backpack")
    inventory_page.add_product_by_name("Sauce Labs Bike Light")
    inventory_page.add_product_by_name("Sauce Labs Bolt T-Shirt")

    assert inventory_page.get_cart_count() == 3

def test_remove_product_from_cart(driver):
    """Test case 6: Xóa sản phẩm khỏi giỏ hàng"""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_product_by_name("Sauce Labs Backpack")
    inventory_page.add_product_by_name("Sauce Labs Bike Light")
    assert inventory_page.get_cart_count() == 2

    inventory_page.go_to_cart()
    cart_page.remove_product_by_name("Sauce Labs Backpack")

    assert cart_page.get_number_of_items() == 1