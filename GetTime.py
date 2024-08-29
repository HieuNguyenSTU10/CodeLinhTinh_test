from datetime import datetime


def get_full():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return current_time


def get_date():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d")
    return current_time


def get_hour():
    now = datetime.now()
    current_time = now.strftime("%H:00:00")
    return current_time


def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def get_minute():
    now = datetime.now()
    current_time = now.strftime("%M")
    return current_time


def get_second():
    now = datetime.now()
    current_time = now.strftime("%S")
    return current_time
