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

## 6. Kết quả kiểm thử (Test Results) & Hình ảnh minh chứng

### 6.1 Tổng quan kết quả
- **Tổng số test cases:** 07
- **Đạt (Passed):** 07 / 07
- **Thất bại (Failed):** 0
- **Tỷ lệ thành công:** 100%

---

### 6.2 Minh chứng chi tiết từng Test Case

> **1. Test Case 1: `test_login_success` (Đăng nhập thành công)**
> <img width="1920" height="952" alt="image" src="https://github.com/user-attachments/assets/ee02e977-798d-451c-b77f-acc6c1253204" />

> **2. Test Case 2: `test_login_failed` (Đăng nhập thất bại)**
> <img width="1920" height="954" alt="image" src="https://github.com/user-attachments/assets/fce06b4f-525e-44ec-88ed-f2f70a152b9d" />

> **3. Test Case 3: `test_login_locked_user` (Đăng nhập tài khoản bị khóa)**
> <img width="1920" height="952" alt="image" src="https://github.com/user-attachments/assets/671f6b44-184b-4f87-91a0-9f1499242e6f" />

> **4. Test Case 4: `test_add_product_to_cart` (Thêm 1 sản phẩm vào giỏ)**
> <img width="1904" height="954" alt="image" src="https://github.com/user-attachments/assets/6dcc85ab-76e1-4489-98de-539f610f7fc8" />

> **5. Test Case 5: `test_add_multiple_products` (Thêm nhiều sản phẩm vào giỏ)**
> <img width="1903" height="953" alt="image" src="https://github.com/user-attachments/assets/dd2151e8-4bf8-44b0-a052-6c535bea84cb" />

> **6. Test Case 6: `test_remove_product_from_cart` (Xóa sản phẩm khỏi giỏ)**
> <img width="1904" height="935" alt="image" src="https://github.com/user-attachments/assets/98af3d44-26ce-433d-8cd7-4845f32896cf" />

> **7. Test Case 7: `test_logout` (Đăng xuất hệ thống)**
> 
> <img width="421" height="307" alt="image" src="https://github.com/user-attachments/assets/7ad87eac-c194-4796-a5fd-1919f4dcd288" />

---

### 6.3 Báo cáo tổng hợp (Report HTML & Terminal)

> **1. Giao diện Website kiểm thử (SauceDemo):**
<img width="1904" height="952" alt="image" src="https://github.com/user-attachments/assets/cd6eb339-600a-4b57-88be-0d68029ae924" />

>
 
> **2. Kết quả thực thi Test Case trong Terminal:**
<img width="1701" height="411" alt="image" src="https://github.com/user-attachments/assets/032f0ce4-fd7a-42e2-81b2-ae58f4146235" />

> 

> **3. Báo cáo kiểm thử HTML (HTML Report):**
<img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/ed7e8515-9012-43fb-ba02-a966c61a7483" />

> 

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
