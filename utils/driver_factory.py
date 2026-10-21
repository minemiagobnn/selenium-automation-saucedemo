from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    # options.add_argument("--headless")  # Bỏ comment nếu muốn chạy ẩn trình duyệt
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    return driver