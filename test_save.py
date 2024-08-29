from import_file import *


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

    return time_save, t_player, t_gold.replace(',', ''), m_player, m_gold.replace(',', ''), win_team, win_gold, time_update


def main():
    try:
        time_save, t_player, t_gold, m_player, m_gold, win_team, win_gold, time_update = read_data_from_file(
            "output.txt")
        new_data = [[time_save, t_player, t_gold, m_player,
                     m_gold, win_team, win_gold, time_update]]
        print(int(t_gold) > int(m_gold))
    except Exception as e:
        print(f"Error occurred: {e}")


main()
