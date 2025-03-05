import re
from collections import Counter
from unicodedata import category

transactions = [
    {"description": "Перевод по номеру телефона", "categories": "Переводы"},
    {"description": "Перевод на карту клиента", "categories": "Переводы"},
    {"description": "Покупка в магазине", "categories": "Оплата"},
    {"description": "Перевод по номеру телефона", "categories": "Переводы"},
    {"description": "Покупка в магазине", "categories": "Оплата"},
    {"description": "Покупка в магазине", "categories": "Оплата"},
    {"description": "Покупка в магазине", "categories": "Оплата"},
    {"description": "Оплата за кредит", "categories": "Списание кредитов"},
]

categories = ["Переводы", "Оплата", "Списание кредитов"]

def search_transactions(transactions, search_string):
    """
    Функция, которая возвращает список словарей, у которых в описании есть нужная строка
    """
    pattern = re.compile(search_string, re.IGNORECASE)
    find_transactions = []
    for i in transactions:
        if "description" in i and pattern.search(i["description"]):
            find_transactions.append(i)
    return find_transactions


def count_transactions(transactions, categories):
    """
    Функция, которая подсчитывает кол-во разных транзакций
    """
    categories_count = Counter()
    for i in transactions:
        if "categories" in i:
            category = i["categories"]
            if category in categories:
                categories_count[category] += 1
    return categories_count

print(search_transactions(transactions, search_string="телефона"))
print(count_transactions(transactions, categories))
