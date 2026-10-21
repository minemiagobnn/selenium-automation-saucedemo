# Báo Cáo Thực Hành Kiểm Thử Tự Động Với Selenium

## 1. Giới thiệu dự án
Dự án này được thực hiện trong khuôn khổ môn học Kiểm thử phần mềm, tập trung vào việc tự tìm hiểu và thực hành công cụ kiểm thử tự động **Selenium WebDriver**.

Mục tiêu chính:
- Nghiên cứu và áp dụng công cụ Selenium để tự động hóa kịch bản kiểm thử.
- Xây dựng **07 test case kiểm thử tự động** hoàn chỉnh cho website thương mại điện tử mẫu [Sauce Demo](https://www.saucedemo.com/).
- Áp dụng mô hình thiết kế **Page Object Model (POM)** giúp quản lý code tối ưu, bảo trì dễ dàng và tái sử dụng tốt.

## 2. Công nghệ & Thư viện sử dụng
- **Ngôn ngữ lập trình:** Python 3.11
- **Thư viện kiểm thử:** Pytest
- **Công cụ Automation:** Selenium WebDriver (Selenium 4.x)
- **Quản lý Driver:** webdriver-manager
- **Báo cáo kết quả:** pytest-html

## 3. Cấu trúc thư mục dự án
```text
selenium-automation-saucedemo/
├── pages/                  # Quản lý các trang theo mô hình POM
│   ├── __init__.py
│   ├── login_page.py       # Quản lý phần tử & hành vi trang Đăng nhập
│   ├── inventory_page.py   # Quản lý phần tử & hành vi trang Danh sách sản phẩm
│   └── cart_page.py        # Quản lý phần tử & hành vi trang Giỏ hàng
├── tests/                  # Chứa toàn bộ các test case kiểm thử
│   ├── __init__.py
│   ├── test_login.py       # Kiểm thử chức năng Đăng nhập & Đăng xuất
│   └── test_cart.py        # Kiểm thử chức năng Giỏ hàng
├── utils/                  # Thư mục chứa các hàm/module hỗ trợ
│   └── __init__.py
├── pytest.ini              # File cấu hình Pytest
├── requirements.txt        # Danh sách thư viện cần thiết
└── README.md               # Tài liệu hướng dẫn dự án

```

## 4. Hướng dẫn cài đặt và khởi chạy

### Bước 1: Tải hoặc clone dự án

```bash
git clone [https://github.com/minemiagobnn/selenium-automation-saucedemo.git](https://github.com/minemiagobnn/selenium-automation-saucedemo.git)
cd selenium-automation-saucedemo

```

### Bước 2: Khởi tạo môi trường ảo và cài đặt dependencies

```bash
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường ảo (Windows)
venv\Scripts\activate

# Cài đặt các thư viện phụ thuộc
pip install -r requirements.txt

```

### Bước 3: Thực thi các Test Case

Chạy toàn bộ 07 test case và xuất báo cáo kiểm thử dạng HTML:

```bash
pytest -v --html=report.html

```

---

## 5. Danh sách 07 Test Case Kiểm Thử Tự Động

Các kịch bản kiểm thử được thiết kế chi tiết bao phủ các chức năng cơ bản của website:

| STT | Tên Test Case | Chức năng kiểm thử | Kết quả mong đợi | Trạng thái |
| --- | --- | --- | --- | --- |
| 1 | `test_login_success` | Đăng nhập tài khoản | Đăng nhập thành công, chuyển hướng vào trang sản phẩm | **Passed** |
| 2 | `test_login_failed` | Đăng nhập thất bại | Hiển thị thông báo lỗi khi nhập sai mật khẩu | **Passed** |
| 3 | `test_login_locked_user` | Đăng nhập tài khoản bị khóa | Hiển thị thông báo tài khoản đã bị khóa | **Passed** |
| 4 | `test_add_product_to_cart` | Thêm 1 sản phẩm | Sản phẩm được thêm thành công, icon giỏ hàng tăng số lượng lên 1 | **Passed** |
| 5 | `test_add_multiple_products` | Thêm nhiều sản phẩm | Thêm 2+ sản phẩm, giỏ hàng cập nhật chính xác số lượng | **Passed** |
| 6 | `test_remove_product_from_cart` | Xóa sản phẩm khỏi giỏ | Xóa thành công, giỏ hàng giảm số lượng hoặc về trống | **Passed** |
| 7 | `test_logout` | Đăng xuất hệ thống | Đăng xuất thành công, chuyển về lại trang Đăng nhập | **Passed** |

---

## 6. Kết quả kiểm thử (Test Results)

* **Tổng số test cases:** 07
* **Đạt (Passed):** 07 / 07
* **Thất bại (Failed):** 0
* **Tỷ lệ thành công:** 100%

---

## 7. Kiến thức tích lũy & Cách xử lý vấn đề

### Kiến thức thu hoạch được

* Nắm vững các locator trong Selenium (ID, Class, XPath, CSS Selector).
* Hiểu và triển khai thành thạo mô hình **Page Object Model (POM)** trong tự động hóa.
* Quản lý và xử lý dữ liệu test động bằng Pytest Fixture.

### Khó khăn & Giải pháp

* **Lỗi thiếu module khi chạy test:** Đã khắc phục bằng cách bổ sung file `__init__.py` vào từng thư mục gói (`pages`, `tests`, `utils`).
* **Lỗi không đẩy được code bằng Terminal máy trường (không có Git/quyền cài đặt):** Khắc phục bằng cách Upload trực tiếp các file/thư mục nguồn lên GitHub qua giao diện trình duyệt web, loại bỏ các thư mục rác/môi trường như `venv` và `.pytest_cache`.

---

## 8. Thông tin sinh viên thực hiện

* **Họ và tên:** Đỗ Vân Khánh
* **Mã số sinh viên (MSSV):** 23013929

```

```
