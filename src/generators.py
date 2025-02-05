def filter_by_currency(not_sort_list, status="USD"):
    for transaction in not_sort_list:
        wallet = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if wallet == status:
            yield transaction


def transaction_descriptions(not_sort_list):
    for transaction in not_sort_list:
        type_transaction = transaction.get("description")
        yield type_transaction



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
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258533",
        "to": "Счет 75651667383060284122"
    }
]

filtered_transactions = filter_by_currency(not_sort_list, status="USD")
for transaction in range(2):
    print(next(filtered_transactions))

descriptions = transaction_descriptions(not_sort_list)
for descrption in range(4):
    print(next(descriptions))
