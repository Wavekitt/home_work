from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(uncorrect_card, correct_card):
    assert get_mask_card_number(" ") == uncorrect_card
    assert get_mask_card_number("1234567812345678") == correct_card


def test_get_mask_account(uncorrect_account, correct_account):
    assert get_mask_account("22811337") == uncorrect_account
    assert get_mask_account("12345678901234567890") == correct_account
