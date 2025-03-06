from typing import Any, Dict, List


def filter_by_state(user_input: List[Dict[str, Any]], status: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    функция, которая возвращает новый список словарей, у которых ключ state соответствует указанному значению
    """
    new_user_input = []
    for i in user_input:
        if i.get("state") == status:
            new_user_input.append(i)
    return new_user_input  # возвращает отсортированный список.


def sort_by_date(user_input: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Функция, которая возвращает список отсортированный по дате.
    """
    sort_date = sorted(user_input, key=lambda x: x["date"], reverse=reverse)
    return sort_date  # возвращает список отсортированный по дате
