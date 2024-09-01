from import_file import *

test = True


def khoi_tao_chrome():
    chrome_options = Options()
    # Đường dẫn đến thư mục chứa profile
    profile_path = f"tk"
    chrome_options.add_argument(f"user-data-dir={profile_path}")
    # Thêm thư mục profile vào các tùy chọn
    chrome_options.add_argument("--headless=new")
    # Khởi chạy Chrome với profile
    driver = webdriver.Chrome(options=chrome_options)
    # driver.minimize_window()
    return driver


def isTest():
    global test
    return test
