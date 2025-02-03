import pytest


@pytest.fixture
def uncorrect_card():
    return "Неверные данные!"


@pytest.fixture
def correct_card():
    return "1234 56** **** 5678"


@pytest.fixture
def uncorrect_account():
    return "Неверные данные!"


@pytest.fixture
def correct_account():
    return "**7890"


@pytest.fixture
def good_account():
    return "Счет **7890"


@pytest.fixture
def good_card():
    return "MasterCard 1234 56** **** 5678"


@pytest.fixture
def good_card_2():
    return "Visa Platinum 1234 56** **** 5678"


@pytest.fixture
def bad_input():
    return "Неверные данные!"


@pytest.fixture
def good_data():
    return "10.11.2012"


@pytest.fixture
def bad_data():
    return "Неверный формат даты!"


@pytest.fixture
def filtred_list_state():
    return [
        {'id': 41428829, 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'}
    ]


@pytest.fixture
def filtred_list_date():
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
