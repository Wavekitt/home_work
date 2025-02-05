import pytest
from typing import List, Dict, Union, Any


@pytest.fixture
def transaction_question() -> List[str]:
    return [
        "Перевод организации"
        "Перевод со счета на счет"
        "Перевод со счета на счет"
        "Перевод от организации"
    ]


@pytest.fixture
def filtred_usd() -> List[Dict[str, Any]]:
    return [
        {
            'id': 939719570, 'state': 'EXECUTED',
            'date': '2018-06-30T02:08:58.425572',
            'operationAmount': {
                'amount': '9824.07', 'currency': {
                    'name': 'USD', 'code': 'USD'
                }
            },
            'description': 'Перевод организации',
            'from': 'Счет 75106830613657916952',
            'to': 'Счет 11776614605963066702'
        },
        {
            'id': 142264268, 'state': 'EXECUTED',
            'date': '2019-04-04T23:20:05.206878',
            'operationAmount': {
                'amount': '79114.93', 'currency': {
                    'name': 'USD', 'code': 'USD'
                }
            },
            'description': 'Перевод со счета на счет',
            'from': 'Счет 19708645243227258542',
            'to': 'Счет 75651667383060284188'
        }
    ]


@pytest.fixture
def filtred_list_state() -> List[Dict[str, Union[int, str]]]:
    return [
        {'id': 41428829, 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'}
    ]


@pytest.fixture
def filtred_list_date() -> List[Dict[str, Union[int, str]]]:
    return [
        {'id': 41428829, 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED',
         'date': '2018-10-14T08:21:33.419441'},
        {'id': 615064591, 'state': 'CANCELED',
         'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': 594226727, 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'}
    ]


@pytest.fixture
def uncorrect_card() -> str:
    return "Неверные данные!"


@pytest.fixture
def correct_card() -> str:
    return "1234 56** **** 5678"


@pytest.fixture
def uncorrect_account() -> str:
    return "Неверные данные!"


@pytest.fixture
def correct_account() -> str:
    return "**7890"


@pytest.fixture
def good_account() -> str:
    return "Счет **7890"


@pytest.fixture
def good_card() -> str:
    return "MasterCard 1234 56** **** 5678"


@pytest.fixture
def good_card_2() -> str:
    return "Visa Platinum 1234 56** **** 5678"


@pytest.fixture
def bad_input() -> str:
    return "Неверные данные!"


@pytest.fixture
def good_data() -> str:
    return "10.11.2012"


@pytest.fixture
def bad_data() -> str:
    return "Неверный формат даты!"
