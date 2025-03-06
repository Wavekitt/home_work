from unittest.mock import mock_open, patch

from src.utils import list_return, summ_transactions


@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_list_return_valid_file(mock_file):
    transactions = list_return("data/operations.json")
    assert transactions == [{"amount": 100, "currency": "USD"}]


@patch("builtins.open", new_callable=mock_open, read_data='')
def test_list_return_empty_file(mock_file):
    transactions = list_return("data/operations.json")
    assert transactions == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_list_return_file_not_found(mock_file):
    transactions = list_return("data/operations.json")
    assert transactions == []


def test_summ_transactions_rub():
    transaction_rub = [{
        'date': '2019-08-26T10:50:58.294041',
        'description': 'Перевод организации',
        'from': 'Maestro 1596837868705199',
        'id': 441945886,
        'operationAmount': {
            'currency': {'code': 'RUB'},
            'amount': '31957.58'
        }
    }]

    assert summ_transactions(transaction_rub) == 31957.58


@patch("src.utils.convertation_curency")
def test_summ_transactions_USD_ok(mock_convertation_curency):
    mock_convertation_curency.return_value = 100.00
    transaction_usd = [{
        'date': '2019-07-03T18:35:29.512364',
        'description': 'Перевод организации',
        'from': 'MasterCard 7158300734726758',
        'id': 41428829,
        'operationAmount': {
            'currency': {'code': 'USD'},
            'amount': '1.00'
        }
    }]

    result = summ_transactions(transaction_usd)

    assert result == 100.00
    mock_convertation_curency.assert_called_once_with("USD", "RUB", 1.00)


@patch("src.utils.convertation_curency")
def test_summ_transactions_USD_wrong(mock_convertation_curency):
    mock_convertation_curency.return_value = "Error"

    transaction_usd = [{
        'date': '2019-07-03T18:35:29.512364',
        'description': 'Перевод организации',
        'from': 'MasterCard 7158300734726758',
        'id': 41428829,
        'operationAmount': {
            'currency': {'code': 'USD'},
            'amount': '1.00'
        }
    }]

    result = summ_transactions(transaction_usd)

    assert result == 0
    mock_convertation_curency.assert_called_once_with("USD", "RUB", 1.00)
