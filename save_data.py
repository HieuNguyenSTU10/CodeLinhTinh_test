from GetTime import *
from str_const import isTest
import time
from source import *


def read_data_from_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Tệp {file_path} không tồn tại.")

    with open(file_path, "r", encoding='utf-8') as f:
        lines = f.readlines()
        if len(lines) < 2:
            raise ValueError("Tệp không chứa đủ dữ liệu.")
        time_save = lines[0].strip()
        t_player, t_gold = lines[1].strip().split(';')
        m_player, m_gold = lines[2].strip().split(';')
        win_team, win_gold = lines[3].strip().split(';')
        time_update = lines[4].strip()

    return time_save, t_player, t_gold, m_player, m_gold, win_team, win_gold, time_update


def append_to_excel(file_path, new_data, t_gold, m_gold):
    # Mở file
    if os.path.exists(file_path):
        # Mở tệp Excel hiện có
        workbook = openpyxl.load_workbook(file_path)
        worksheet1 = workbook['DuLieu']

        # Tìm hàng trống cuối cùng (tránh trường hợp hàng có dữ liệu trống)
        last_row = worksheet1.max_row
        while last_row > 0 and not any(cell.value for cell in worksheet1[last_row]):
            last_row -= 1
        start_row = last_row + 1
    else:
        # Nếu tệp không tồn tại, tạo mới tệp Excel
        workbook = openpyxl.Workbook()
        worksheet1 = workbook.active
        start_row = 1

    # Lưu sheet dữ liệu
    for i, row in enumerate(new_data, start=start_row):
        for j, value in enumerate(row, start=1):
            # Đảm bảo giá trị là kiểu dữ liệu hợp lệ
            if isinstance(value, list):
                value = str(value)  # Chuyển danh sách thành chuỗi
            worksheet1.cell(row=i, column=j, value=value)

    worksheet2 = workbook['KetQua']
    # Luu sheet kết quả
    last_row = worksheet2.max_row
    while last_row > 0 and not any(cell.value for cell in worksheet2[last_row]):
        last_row -= 1
    start_row = last_row

    value1 = worksheet2.cell(row=start_row, column=1).value
    value2 = worksheet2.cell(row=start_row, column=25).value
    date = None

    # kiem tra ngay hien tai
    if (start_row == 2 or value2 not in (None, '')):
        start_row += 1
        date = get_date()
        worksheet2.cell(row=start_row, column=1, value=date)

    win_team = new_data[0][5]

    col = int(get_hour().strip().split(':')[0]) + 2
    str = win_team.strip().split(" ")[0]
    sosang = "Lớn" if ((str == "Tiên" and (int(t_gold) >= int(m_gold))) or (
        str == "Ma" and (int(m_gold) >= int(t_gold)))) else "Nhỏ"

    value_save = str + " - " + sosang
    worksheet2.cell(row=start_row, column=col, value=value_save)
    print(col, value_save)

    # Lưu tệp Excel
    workbook.save(file_path)


def main_save():
    main_source()
    try:
        time_save, t_player, t_gold, m_player, m_gold, win_team, win_gold, time_update = read_data_from_file(
            "output.txt")
        new_data = [[time_save, t_player, t_gold, m_player,
                     m_gold, win_team, win_gold, time_update]]
        append_to_excel('data.xlsx', new_data, t_gold.replace(
            ',', ''), m_gold.replace(',', ''))
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    minute, second = 58, 30
    print(f"start {get_time()}", flush=True)
    check = isTest()
    if (check == True):
        while True:
            cminute = int(get_minute())
            csecond = int(get_second())
            # if (cminute == minute and csecond == second):
            #     main()
            # else:
            #     time.sleep(1)

            if (cminute < minute and csecond < second):
                time.sleep(60)
            elif ((cminute == minute and csecond < second) or (cminute < minute and csecond > second)):
                print(f"{get_time()}", flush=True)
                time.sleep(1)
            elif (csecond == second):
                main_save()
    else:
        main_save()
