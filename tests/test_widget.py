from src.widget import mask_account_card, get_date


def test_mask_account_card(good_account, good_card, good_card_2, bad_input):
    assert mask_account_card("Счет 12345678901234567890") == good_account
    assert mask_account_card("MasterCard 1234567812345678") == good_card
    assert mask_account_card("Visa Platinum 1234567812345678") == good_card_2
    assert mask_account_card("Visa Sber Platina 1234567812345678") == bad_input
    assert mask_account_card("wedfghjk 568712") == bad_input


def test_get_data(good_data, bad_data):
    assert get_date("2012-11-10T01:02:03.012345") == good_data
    assert get_date("26 ноября две тыcячи двенадцатого") == bad_data
