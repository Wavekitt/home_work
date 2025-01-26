def filter_by_state(user_input, status="EXECUTED"):
    """
    функция, которая возвращает новый список словарей, у которых ключ state соответствует указанному значению
    """
    new_user_input = []
    try:
        for i in user_input:
            if i.get("state") == status:
                new_user_input.append(i)
        return new_user_input  # возвращает отсортированный список
    except KeyError:
        return "Неверные данные"  # возвращает, если вводные данные неверны


def sort_by_date(user_input):
    """
    Функция, которая возвращает список отсортированный по дате.
    """
    sort_date = sorted(user_input, key=lambda x: x["date"], reverse=True)
    return sort_date  # возвращает список отсортированный по дате


# входные данные для проверки, можно их удалить или закомментировать
user_input = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
              {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
              {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
              {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
              {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
              {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
