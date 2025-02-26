import os
from typing import Optional
import requests
from dotenv import load_dotenv
from webbrowser import Error

load_dotenv("../.env")

api_key = os.getenv("API_KEY")


def convertation_curency(currency: str, rub: str, amount: float) -> Optional[float]:
    """
    функция, которая конвертирует валюты
    """
    url = (
        f"https://api.apilayer.com/exchangerates_data/convert?"
        f"to={rub}&from={currency}&amount={amount}&apikey={api_key}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()["result"]
        return result
    else:
        return "Error"
