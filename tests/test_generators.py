import pytest

from typing import List, Dict, Any

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(filtred_usd: List[dict]) -> None:
    test_usd = [
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
    assert filter_by_currency(test_usd)


def test_transaction_descriptions(transaction_question: List[Dict[str, Any]]) -> None:
    test_transaction = [
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
    assert transaction_descriptions(test_transaction)


@pytest.mark.parametrize("start, stop, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (4, 4, ["0000 0000 0000 0004"]),
    (7, 7, ["0000 0000 0000 0007"]),
    (2200, 2200, ["0000 0000 0000 2200"]),
    (123, 123, ["0000 0000 0000 0123"]),
    (13, 16, [
        "0000 0000 0000 0013",
        "0000 0000 0000 0014",
        "0000 0000 0000 0015",
        "0000 0000 0000 0016"
        ]),
    ])
def test_card_number_generator(start: int, stop: int, expected: List[str]) -> None:
    generate_card = list(card_number_generator(start, stop))
    assert generate_card == expected
