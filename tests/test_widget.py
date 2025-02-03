from src.widget import mask_account_card, get_date

import pytest


@pytest.mark.parametrize("card_or_acc, expected", [
        ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
        ("Visa Platinum 1234567812345678", "Visa Platinum 1234 56** **** 5678"),
        ("wedfghjk 568712", "Неверные данные!"),
        ("sffggh ssdaf 1234", "Неверные данные!"),
        ("Visa Sber Platina 1234567812345678", "Неверные данные!"),
        (" ", "Неверные данные!"),
        ("Cxtn 12345678901234567890", "Неверные данные!"),
])
def test_mask_account_card(card_or_acc: str, expected: str) -> None:
    assert mask_account_card(card_or_acc) == expected


@pytest.mark.parametrize("date_correct, expected", [
        ("2012-11-10T01:02:03.012345", "10.11.2012"),
        ("2012.11.10.02:03", "Неверный формат даты!"),
])
def test_get_date(date_correct: str, expected: str) -> None:
    assert get_date(date_correct) == expected
