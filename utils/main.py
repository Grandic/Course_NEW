from utils.funcions import five_operations, good_time, hide_card, load_json


def main_function(name=None):
    """Функция которая выводит на экран
    список из 5 последних выполненных клиентом операций
    name = load_json, или иная функция загрузки данных или просто данные
    в данной ситуации я присвою ей аргумент, чтобы было понятнее"""
    name = load_json()
    for j in five_operations(name):
        for i in name:
            if "date" in i and i["date"] == j:
                operation = f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}'
                print(f'{good_time(i["date"])} {i["description"]}')
                if 'открытие' in i['description'].lower():
                    print(f'{hide_card(i["to"])}')
                else:
                    print(f'{hide_card(i["from"])} -> {hide_card(i["to"])}')
                print(operation)
                print()

