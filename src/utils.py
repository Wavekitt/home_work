import json
from src.external_api import convertation_curency

file_path = "data/operations.json"


def list_return(file_path: str) -> list:
    """
    Функция, которая берет JSON файл и возвращает список словарей
    """
    try:
        with open(file_path, encoding='utf-8', errors='ignore') as f:
            try:
                transaction_list = json.load(f)
            except json.JSONDecodeError:
                print("Файл не декодируется")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []
    return transaction_list


def summ_transactions(transaction_list: dict) -> float:
    """
    Функция, которая возвращает сумму транзакций в рублях.
    """
    currency = transaction_list["operationAmount"]["currency"]["code"]
    amount = transaction_list["operationAmount"]["amount"]
    if currency == "RUB":
        return amount
    else:
        alternative_summ = convertation_curency(currency, "RUB", amount)
        return alternative_summ
