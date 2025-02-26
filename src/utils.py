import json
from src.external_api import convertation_curency

file_path = "../data/operations.json"


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
    # all_sum = 0
    # for i in transaction_list:
    #     try:
    #         currency = i["operationAmount"]["currency"]["code"]
    #         amount = i["operationAmount"]["amount"]
    #         if currency == "RUB":
    #             all_sum += float(amount)
    #         else:
    #             alternative_summ = convertation_curency(currency, "RUB", amount)
    #             all_sum += float(alternative_summ)
    #     except KeyError:
    #         all_sum += 0
    # return all_sum

print(summ_transactions(transaction_list=list_return(file_path)))