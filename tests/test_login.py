import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_login_success(driver):
    """Test case 1: Đăng nhập thành công"""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_loaded() == True
    assert "inventory" in driver.current_url

def test_login_failed(driver):
    """Test case 2: Đăng nhập thất bại với mật khẩu sai"""
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("standard_user", "wrong_password")

    error = login_page.get_error_message()
    assert "Username and password do not match" in error

def test_login_locked_user(driver):
    """Test case 3: Đăng nhập với tài khoản bị khóa"""
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    error = login_page.get_error_message()
    assert "Sorry, this user has been locked out" in error

def test_logout(driver):
    """Test case 7: Đăng xuất thành công"""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.is_loaded()

    inventory_page.logout()
    assert "saucedemo.com" in driver.current_url
    assert driver.find_element("id", "login-button").is_displayed()