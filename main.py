import json
import csv
import pandas as pd
from src.transactions_file import read_financial_operations_from_csv, read_financial_operations_from_excel


def main():
    print(f"Привет! Добро пожаловать в программу работы \nс банковскими транзакциями."
          f"Выберите необходимый пункт меню:"
          f"1. Получить информацию о транзакциях из JSON-файла."
          f"2. Получить информацию о транзакциях из CSV-файла."
          f"3. Получить информацию о транзакциях из XLSX-файла.")

    user_input = (str(input("Напиши номер варианта, который тебе нужен. ")))
    if user_input == "1":
        print("1. Получить информацию о транзакциях из JSON-файла")
    elif user_input == "2":
        print("2. Получить информацию о транзакциях из CSV-файла")
    elif user_input == "3":
        print("3. Получить информацию о транзакциях из XLSX-файла")
    else:
        print("Некорректный выбор")

    status = {"EXECUTED", "CANCELED", "PENDING"}
    status_input = input("Введите статус, для фильтрации. \nДоступные статусы: EXECUTED, CANCELED, PENDING")
    if status_input.upper() in status:
        print(f"Сортировка по статусу {status_input}")
    else:
        print(f"Статус операции {status_input} недоступен")
    input_choise = input("Отсортировать по дате? Да\Нет")
    if input_choise == "Да":
        input_choise_2 = input("по возрастанию\по убыванию")
        if input_choise_2 == ""

