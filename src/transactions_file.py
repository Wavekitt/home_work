import csv
from typing import Dict, List

import pandas as pd


def read_financial_operations_from_csv(filepath: str) -> List[Dict]:
    transactions = []
    with open(filepath, mode="r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            transactions.append(row)
    return transactions


def read_financial_operations_from_excel(filepath: str) -> List[Dict]:
    df = pd.read_excel(filepath)
    return df.to_dict(orient="records")


if __name__ == "__main__":
    csv_file_path = r"C:\Users\wavekitt\Desktop\transactions.csv"
    excel_file_path = r"C:\Users\wavekitt\Desktop\transactions_excel.xlsx"

    transactions_from_csv = read_financial_operations_from_csv(csv_file_path)
    transactions_from_excel = read_financial_operations_from_excel(excel_file_path)

    print(transactions_from_csv)
    print(transactions_from_excel)