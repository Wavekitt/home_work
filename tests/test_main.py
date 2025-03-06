from unittest.mock import patch
import main


@patch("builtins.input", side_effect=["1", "EXECUTED", "нет", "нет", "нет"])
@patch("main.list_return", return_value=[
    {
        "date": "2024-03-06",
        "description": "Перевод",
        "state": "EXECUTED",
        "operationAmount": {"amount": 5000, "currency": {"name": "RUB"}},
        "from": "Счет 1234567890123456",
        "to": "Счет 9876543210987654"
    }
])
def test_main_json(mock_list_return, mock_input, capsys):
    main.main()

    captured = capsys.readouterr()

    assert "Привет! Добро пожаловать в программу работы с банковскими транзакциями." in captured.out
    assert "Для обработки выбран JSON-файл." in captured.out
    assert "Операции отфильтрованы по статусу \"EXECUTED\"" in captured.out
    assert "Распечатываю итоговый список транзакций..." in captured.out
    assert "Всего банковских операций в выборке: 1" in captured.out
    assert "2024-03-06 Перевод" in captured.out


@patch("builtins.input", side_effect=["3", "EXECUTED", "нет", "нет", "нет"])
@patch("main.read_financial_operations_from_excel", return_value=[
    {
        "date": "2024-03-01",
        "description": "Кредит",
        "state": "EXECUTED",
        "amount": 1000,
        "currency_name": "RUB",
        "from": "Счет 1234567890123456",  # Добавляем from
        "to": "Счет 9876543210987654"    # Добавляем to
    }
])
def test_main_excel(mock_excel, mock_input, capsys):
    with patch("builtins.print") as mock_print:
        main.main()
        mock_print.assert_any_call("Для обработки выбран XLSX-файл.")
        mock_print.assert_any_call("Операции отфильтрованы по статусу \"EXECUTED\"")
        mock_print.assert_any_call("Распечатываю итоговый список транзакций...")
        mock_print.assert_any_call("Всего банковских операций в выборке: 1")


@patch("builtins.input", side_effect=["3", "EXECUTED", "нет", "нет", "нет"])
@patch("main.read_financial_operations_from_excel", return_value=[
    {
        "date": "2024-03-01",
        "description": "Кредит",
        "state": "EXECUTED",
        "amount": 1000,
        "currency_name": "RUB",
        "from": "Счет 1234567890123456",
        "to": "Счет 9876543210987654"
    }
])
def test_main_xlsx(mock_xlsx, mock_input, capsys):
    with patch("builtins.print") as mock_print:
        main.main()
        mock_print.assert_any_call("Для обработки выбран XLSX-файл.")
