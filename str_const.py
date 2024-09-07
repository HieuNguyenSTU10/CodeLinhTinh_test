from import_file import *

test = False


def khoi_tao_chrome():
    chrome_options = Options()
    # Đường dẫn đến thư mục chứa profile
    # profile_path = f"F:\\Game\\FolderCode\\CodeLinhTinh_test\\tk"
    profile_path = f"tk"
    chrome_options.add_argument(f"user-data-dir={profile_path}")
    # Thêm thư mục profile vào các tùy chọn
    chrome_options.add_argument("--headless=new")
    # Vô hiệu hóa GPU (có thể cần trên môi trường headless)
    chrome_options.add_argument("--disable-gpu")
    # Thường cần khi chạy trên môi trường không có GUI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Khởi chạy Chrome với profile
    driver = webdriver.Chrome(options=chrome_options)
    # driver.minimize_window()
    return driver


def isTest():
    global test
    return test
