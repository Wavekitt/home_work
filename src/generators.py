def filter_by_currency(not_sort_list, status="USD"):
    for transaction in not_sort_list:
        currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if currency_code == status:
            yield transaction


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

filtered_transactions = filter_by_currency(not_sort_list, status="RUB")

for transaction in range(2):
    print(next(filtered_transactions))
