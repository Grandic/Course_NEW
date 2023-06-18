import json
from datetime import datetime


def load_json():
    """Функция получает расположение Json-файла и преобразует его в словарь"""
    with open("operations.json", "r", encoding="UTF=8") as read_file:
        operations = json.load(read_file)
        return operations


def five_operations(file):
    """Функция сортирует список по наличию даты операции и ее выполнению
    и создает новый список с датами последних 5 операций"""
    date_list = []
    for i in file:
        if "date" in i and i["state"] == "EXECUTED":
            date_list.append(i["date"])
        date_list.sort(reverse=True)
    return date_list[:5]


def good_time(time_string):
    """Функция форматирует время из файла под нужный нам формат"""
    time_time = datetime.strptime(time_string, '%Y-%m-%dT%H:%M:%S.%f')
    time_string_new = time_time.strftime("%d-%m-%Y")
    return time_string_new


def hide_card(payment):
    """Функция скрывает данные карты или счета проверяя тип данных"""
    if "счет" in payment.lower():
        return f'{payment[:5]}**{payment[-4:]}'
    else:
        payment_type = f'{payment.split()[len(payment.split()) - 1]}'
        card_type = f'{payment.replace(f" {payment_type}", "")}'
        payment_type = payment_type[:-10] + '** **** ' + payment_type[12:]
        payment_type = f'{card_type} {payment_type[:4]} {payment_type[4:]}'
        return payment_type
