from typing import Dict, Generator, List


def filter_by_currency(not_sort_list: List[Dict], status: str = "USD") -> Generator[Dict, None, None]:
    """
    функция, которая сортирует по виду валюты
    """
    for transaction in not_sort_list:
        wallet = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if wallet == status:
            yield transaction  # узнаем тип валюты


def transaction_descriptions(not_sort_list: List[Dict]) -> Generator[str, None, None]:
    """
    функция, которая выводит тип транзакции
    """
    for transaction in not_sort_list:
        type_transaction = transaction.get("description", "")
        yield type_transaction  # узнаем тип транзакции


def card_number_generator(start: int = 0, stop: int = 999999999999) -> Generator[str, None, None]:
    """
    функция, которая генерирует номер карты
    """
    card_without_number = "0000000000000000"
    for i in range(start, stop + 1):
        card_number = str(f"{card_without_number[:-len(str(i))]}{i}")
        yield f"{str(card_number[0:4])} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"  # получаем карту


# список транзакций, нужен, для проверки
not_sort_list = [
    {
        "id": 939719570, "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount":
            {
                "amount": "9824.07",
                "currency":
                    {
                        "name": "USD",
                        "code": "USD"
                    }
            },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount":
            {
                "amount": "79114.93",
                "currency":
                    {
                        "name": "USD",
                        "code": "USD"
                    }
            },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 142214342,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount":
            {
                "amount": "79114.93",
                "currency":
                    {
                        "name": "RUB",
                        "code": "RUB"
                    }
            },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258533",
        "to": "Счет 75651667383060284122"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount":
            {
                "amount": "79114.93",
                "currency":
                    {
                        "name": "RUB",
                        "code": "RUB"
                    }
            },
        "description": "Перевод от организации",
        "from": "Счет 19708645243227258533",
        "to": "Счет 75651667383060284122"
    }
]

# Фильтрация транзакций по валюте
filtered_transactions = filter_by_currency(not_sort_list, status="USD")
for transaction in range(2):
    print(next(filtered_transactions))


# Получение описаний транзакций
descriptions = transaction_descriptions(not_sort_list)
for description in range(4):
    print(next(descriptions))


# Генерация номеров карт
for new_card in card_number_generator(1, 5):
    print(new_card)
