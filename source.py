from str_const import *


t_player, t_gold = '', ''
m_player, m_gold = '', ''
win_team, win_gold = '', ''

driver = None


def login_web():
    global driver
    driver = khoi_tao_chrome()
    web = 'https://cmangaog.com/user/game/dashboard'
    driver.get(web)
    print('truy cap thanh cong', flush=True)


def refresh_web():
    driver.close()
    login_web()  # Sử dụng refresh() thay vì close() và mở lại


def click_button(by, xpath):
    action = False
    div = 0
    while not action:
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((by, xpath)))
            button = driver.find_element(by, xpath)
            # Sử dụng JavaScript để click
            driver.execute_script("arguments[0].click();", button)
            print('click thanh cong')
            action = True
        except TimeoutException:
            print(f"Timeout while trying to click {xpath}")
            div += 1
            driver.refresh()
            time.sleep(1)
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(1)
            return 1
        if (div == 5):
            return 1


def login():
    while click_button(By.CLASS_NAME, 'text_button_login') == 1:
        print("refeat")
        driver.refresh()
    time.sleep(3)
    search_box = driver.find_element(By.ID, 'login_username')
    search_box.send_keys('duykhag604')
    search_box = driver.find_element(By.ID, 'login_password')
    search_box.send_keys('duykhag604@')
    search_box.send_keys(Keys.RETURN)
    print('dang nhap thanh cong', flush=True)
    time.sleep(3)


def get_text(by, tstring):
    try:
        element = driver.find_element(by, tstring)
        stext = element.text
        return stext
    except NoSuchElementException:
        print(f"Element with {By.XPATH} and {tstring} not found.")
        return ''


def get_nguoi_vang():
    result1, result2, result3, result4 = '', '', '', ''
    time.sleep(3)
    (result1, result2) = (get_text(By.XPATH, "//div[@class='angel top child_module']//div[@class='statics']//p//span[@class='player']"),
                          get_text(By.XPATH, "//div[@class='angel top child_module']//div[@class='statics']//p//span[@class='gold']"))
    (result3, result4) = (get_text(By.XPATH, "//div[@class='devil top child_module']//div[@class='statics']//p//span[@class='player']"),
                          get_text(By.XPATH, "//div[@class='devil top child_module']//div[@class='statics']//p//span[@class='gold']"))
    (player, gold) = (result1 + result3, result2 + result4)
    return player, gold


def ket_qua():
    global win_team, win_gold
    button = driver.find_element(
        By.XPATH, '//div[@onclick="load_module(\'content\',\'game/activity/angel_devil\')"]')
    driver.execute_script("arguments[0].click();", button)

    time.sleep(3)
    button1 = driver.find_element(
        By.XPATH, '//button[@onclick="popup_load(\'game/angel_devil/history\')"]')
    button1.click()
    time.sleep(2)
    # print("click")
    while get_text(By.XPATH, "//div[@class='history_list']//table[@class='main_table']//tbody//tr[1]//td[1]") not in ('Ma Giới', 'Tiên Giới'):
        time.sleep(1)
    (win_team, win_gold) = (get_text(By.XPATH, "//div[@class='history_list']//table[@class='main_table']//tbody//tr[1]//td[1]"),
                            get_text(By.XPATH, "//div[@class='history_list']//table[@class='main_table']//tbody//tr[1]//td[3]//span"))


def lay_du_lieu():
    global t_player, t_gold, m_player, m_gold
    click_button(
        By.XPATH, '//div[@onclick="load_module(\'content\',\'game/activity/angel_devil\')"]')
    (t_player, t_gold) = get_nguoi_vang()
    try:
        element = driver.find_element(By.CSS_SELECTOR, '.item.text_ad_devil')
        driver.execute_script("arguments[0].click();", element)
        (m_player, m_gold) = get_nguoi_vang()
        print('lay du lieu thanh cong', flush=True)
    except Exception as e:
        print(f"Error clicking element: {e}")


def save_data():
    global t_player, t_gold, m_player, m_gold, win_team
    time_save = get_date() + " " + get_hour()
    time_update = get_full()
    with open("output.txt", "w", encoding='utf-8') as f:
        f.write(f"{time_save}\n")
        f.write(f"{t_player};{t_gold}\n")
        f.write(f"{m_player};{m_gold}\n")
        f.write(f"{win_team};{win_gold}\n")
        f.write(f"{time_update}\n")


def checklogin():
    time.sleep(5)
    try:
        button = driver.find_element(By.CLASS_NAME, 'text_button_login')
        if (button.text == 'Đăng nhập'):
            return True
        else:
            return False
    except NoSuchElementException:
        return False


def run_retry(func, max_retries=10):
    retries = 0
    while retries < max_retries:
        try:
            func()
            break
        except Exception as e:
            driver.refresh()
            retries += 1
            print(f"Lỗi:. Đang thử lại ({
                  retries}/{max_retries})... {func.__name__}", flush=True)
            if retries == max_retries:
                print("Thất bại sau nhiều lần thử.", flush=True)
            time.sleep(5)


def main_source():
    a = isTest()
    login_web()
    time.sleep(5)
    if (checklogin()):
        run_retry(login)
    while ((int(get_minute()) != 59 or ((int(get_minute()) == 59 and int(get_second()) != 30))) and a == True):
        time.sleep(1)
    print(f"{get_time()}", flush=True)
    run_retry(lay_du_lieu)
    while (int(get_minute()) != 2 and a == True):
        time.sleep(5)
    driver.refresh()
    time.sleep(10)
    run_retry(ket_qua)
    save_data()
    driver.quit()  # Đóng trình duyệt khi hoàn tất
    print(f"luu thanh cong {get_time()}", flush=True)

main_source()
