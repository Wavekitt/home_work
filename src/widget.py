from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_account_number: str):
    """
    Функция, которая определяет счет или номер карты и в зависимости от этого маскирует
    введенные данные.
    """
    first_word = card_account_number.split(" ")[0]
    masked_nums = card_account_number.split(" ")[-1]
    chek_words = len(card_account_number.split(" "))

    if first_word == "Счет":
        result = get_mask_account(masked_nums)
        return f"{first_word} {result}"  # возвращает замаскированный счет

    elif first_word != "Счет" and chek_words in [2, 3]:
        if chek_words == 2:
            type_card = first_word
        elif chek_words == 3:
            type_card = " ".join([first_word, card_account_number.split(" ")[1]])

        number_card = get_mask_card_number(masked_nums)
        if number_card == "Неверные данные!":
            return number_card

        result = " ".join([type_card, number_card])
        return result  # возвращает замаскированную карту

    else:
        return "Неверные данные!"


def get_date(input_date: str):
    """
    Функция, которая принимает дату и возвращает более понятную дату.
    """
    if len(input_date) == 26:
        year_card = input_date[0:4]
        month_card = input_date[5:7]
        day_card = input_date[8:10]
        result = ".".join([day_card, month_card, year_card])
        return result  # возвращает готовую дату

    else:
        return "Неверный формат даты!"  # возвращает при неверных данных
