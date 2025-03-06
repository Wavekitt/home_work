import os
import re

from src.generators import filter_by_currency
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.transactions_file import (
    read_financial_operations_from_csv,
    read_financial_operations_from_excel,
)
from src.utils import list_return


def main():
    """
    Функция, которая отвечает за основную логику проекта и связывает функциональности между собой.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    menu = int(input("""Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    : """))
    if menu == 1:
        print("Для обработки выбран JSON-файл.")
        path_to_file = os.path.join(os.path.dirname(__file__), "data", "operations.json")
        trans = list_return(path_to_file)

    elif menu == 2:
        print("Для обработки выбран CSV-файл.")
        path = os.path.join(os.path.dirname(__file__), "data", "transactions.csv")
        trans = read_financial_operations_from_csv(path)

    else:
        print("Для обработки выбран XLSX-файл.")
        path = os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")
        trans = read_financial_operations_from_excel(path)
    state = input("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.
    """)
    state = state.upper()
    while state not in ['EXECUTED', 'CANCELED', 'PENDING']:
        print(f'Статус операции "{state}" недоступен.')
        state = input("""Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы:
        :""")
        state = state.upper()
    else:
        if state == "EXECUTED":
            print('Операции отфильтрованы по статусу "EXECUTED"')
        elif state == 'CANCELED':
            print('Операции отфильтрованы по статусу "CANCELED"')
        else:
            print('Операции отфильтрованы по статусу "PENDING"')

    filter_trans = filter_by_state(trans, state)

    data_filter = input("""Отсортировать операции по дате? Да/Нет: """).lower()
    while data_filter not in ['да', 'нет']:
        print('Пожалуйста, введите "Да" или "Нет".')
        data_filter = input("Отсортировать операции по дате? Да/Нет: ").lower()

    if data_filter == 'да':
        sort = input("""Отсортировать по возрастанию или по убыванию?: """).lower()
        while sort not in ['по возрастанию', 'по убыванию']:
            print('Пожалуйста, введите "по возрастанию" или "по убыванию".')
            sort = input("Отсортировать по возрастанию или по убыванию?: ").lower()
        sort_key = sort == 'по убыванию'
        new_filter_trans = sort_by_date(filter_trans, sort_key)
    else:
        new_filter_trans = filter_trans

    code = input("""Выводить только рублевые тразакции? Да / Нет: """).upper()
    while code not in ['ДА', 'НЕТ']:
        print('Пожалуйста, введите "Да" или "Нет".')
        code = input("Выводить только рублевые тразакции? Да / Нет: ").upper()
    if code == 'ДА':
        new_filter_trans = filter_by_currency(new_filter_trans, 'RUB')

    filter_word = input("""Отфильтровать список транзакций по определенному слову в описании? Да/Нет: """).lower()
    while filter_word not in ['да', 'нет']:
        print('Пожалуйста, введите "Да" или "Нет".')
        filter_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if filter_word == 'да':
        word = input("Введите слово для фильтрации: ")
        new_filter_trans = [x for x in new_filter_trans if word.lower() in x.get("description", "").lower()]

    print('Распечатываю итоговый список транзакций...')

    if not any(new_filter_trans):
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
        return

    print(f'Всего банковских операций в выборке: {len(new_filter_trans)}')

    if menu == 1:
        for x in new_filter_trans:
            if x.get("description") == "Открытие вклада":
                print(f'{x["date"]} {x["description"]}')
                pattern = r'\b\d+\b'
                numer = re.findall(pattern, x["to"])
                numer = ''.join(numer)
                print(f'Счет{get_mask_account(numer)}')
                print(f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}')
            else:
                print(f'{x["date"]} {x["description"]}')
                pattern = r'\b\d+\b'
                pattern1 = r'\b[A-Za-zА-Яа-яЁё]+\b'

                text = x["from"]
                numer_from = re.findall(pattern, text)
                numer_from = ''.join(numer_from)
                name_from = re.findall(pattern1, text)
                name_from = ''.join(name_from)

                text_to = x["to"]
                numer_to = re.findall(pattern, text_to)
                numer_to = ''.join(numer_to)
                name_to = re.findall(pattern1, text_to)
                name_to = ''.join(name_to)

                if name_from == 'Счет':
                    numer_from_mask = get_mask_account(numer_from)
                else:
                    numer_from_mask = get_mask_card_number(numer_from)
                if name_to == 'Счет':
                    numer_to_mask = get_mask_account(numer_to)
                else:
                    numer_to_mask = get_mask_card_number(numer_to)
                print(f'{name_from} {numer_from_mask} -> {name_to} {numer_to_mask}')
                print(f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}')
    else:
        for x in new_filter_trans:
            if x.get("description") == "Открытие вклада":
                print(f'{x["date"]} {x["description"]}')
                pattern = r'\b\d+\b'
                numer = re.findall(pattern, x["to"])
                numer = ''.join(numer)
                print(f'Счет{get_mask_account(numer)}')
                print(f'Сумма: {x["amount"]} {x["currency_name"]}')
            else:
                print(f'{x["date"]} {x["description"]}')
                pattern = r'\b\d+\b'
                pattern1 = r'\b[A-Za-zА-Яа-яЁё]+\b'

                text = x["from"]
                numer_from = re.findall(pattern, text)
                numer_from = ''.join(numer_from)
                name_from = re.findall(pattern1, text)
                name_from = ''.join(name_from)

                text_to = x["to"]
                numer_to = re.findall(pattern, text_to)
                numer_to = ''.join(numer_to)
                name_to = re.findall(pattern1, text_to)
                name_to = ''.join(name_to)

                if name_from == 'Счет':
                    numer_from_mask = get_mask_account(numer_from)
                else:
                    numer_from_mask = get_mask_card_number(numer_from)
                if name_to == 'Счет':
                    numer_to_mask = get_mask_account(numer_to)
                else:
                    numer_to_mask = get_mask_card_number(numer_to)
                print(f'{name_from} {numer_from_mask} -> {name_to} {numer_to_mask}')
                print(f'Сумма: {x["amount"]} {x["currency_name"]}')


if __name__ == '__main__':
    main()
