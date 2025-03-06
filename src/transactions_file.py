from typing import Dict, List

import pandas as pd


def read_financial_operations_from_csv(csv_file_path: str) -> List[Dict]:
    """
    функиця, которая считывает из csv файла и возвращает список словарей с транзакциями.
    """
    try:
        csv_data = pd.read_csv(csv_file_path, delimiter=";")
        operations_data = csv_data.to_dict(orient="records")
    except pd.errors.EmptyDataError:
        print(f"Файл {csv_file_path} не найден")
        return []
    except FileNotFoundError:
        print(f"Файл {csv_file_path} не найден")
        return []
    return operations_data


def read_financial_operations_from_excel(filepath: str) -> List[Dict]:
    """
    Функция принимает на вход путь к файлу Excel и возвращает список словарей с транзакциями.
    """
    df = pd.read_excel(filepath)
    return df.to_dict(orient="records")


if __name__ == "__main__":
    csv_file_path = r"C:\Users\wavekitt\PythonProject4\data\transactions.csv"
    excel_file_path = r"C:\Users\wavekitt\PythonProject4\data\transactions_excel.xlsx"

    transactions_from_csv = read_financial_operations_from_csv(csv_file_path)
    transactions_from_excel = read_financial_operations_from_excel(excel_file_path)

    print(transactions_from_csv)
    print(transactions_from_excel)
