import pytest
from src.masks import get_mask_card_number, get_mask_account

# Тесты для функции get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1234123412341234", "1234 12** **** 1234"),
        ("123412341234", "Неверные данные!"),
        ("12345678901234567890", "Неверные данные!"),
        (" ", "Неверные данные!"),
    ]
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# Тесты для функции get_mask_account
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678901234567890", "**7890"),
        ("12345678901234", "Неверные данные!"),
        ("12345", "Неверные данные!"),
        (" ", "Неверные данные!"),
    ]
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected