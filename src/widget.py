from masks import get_mask_card_number, get_mask_account


def mask_account_card(card_account_number):
    """
    функция которая определяет счет или номер карты и в зависимости этого маскирует введенные данные.
    """
    first_word = (card_account_number.split(" ")[0]).title
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
        result = " ".join([type_card, number_card])
        return result  # возвращает замаскированную карту


def get_date(input_date):
    """
    функция которая принимает дату и возвращает более понятную дату.
    """
    year_card = input_date[0:4]
    mounth_card = input_date[5:7]
    day_card = input_date[8:10]
    result = ".".join([day_card, mounth_card, year_card])
    return result  # возвращает готовую дату


input_date = input("Введите дату карты: ")


card_account_number = input("Введите тип и номер карты или ваш Счет: ")
