from collections import Counter
from src.search_transactions import search_transactions, count_transactions


def test_search_transactions_found(sample_transactions):
    result = search_transactions(sample_transactions, "Перевод")
    assert len(result) == 3
    assert all("Перевод" in item["description"] for item in result)


def test_search_transactions_not_found(sample_transactions):
    result = search_transactions(sample_transactions, "Невозможно найти")
    assert result == []


def test_count_transactions(sample_transactions, sample_categories):
    result = count_transactions(sample_transactions, sample_categories)
    expected = Counter({"Переводы": 3, "Оплата": 4, "Списание кредитов": 1})
    assert result == expected
