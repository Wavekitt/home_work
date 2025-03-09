import json
import logging
import os

from src.external_api import convertation_curency

log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(log_dir, exist_ok=True)
log_file_utils = os.path.join(log_dir, "utils_log.log")
logger = logging.getLogger("utils_log")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file_utils, "w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

file_path = "../data/operations.json"


def list_return(file_path: str) -> list:
    """
    Функция, которая берет JSON файл и возвращает список словарей
    """
    logger.info("работаем со словарем")
    try:
        with open(file_path, encoding='utf-8', errors='ignore') as f:
            try:
                transaction_list = json.load(f)
            except json.JSONDecodeError:
                logger.error("Файл не декодируется")
                print("Файл не декодируется")
                return []
    except FileNotFoundError:
        logger.error("файл не найден")
        print("Файл не найден")
        return []
    logger.info(f"получаем результат {transaction_list}")
    return transaction_list


def summ_transactions(transaction_list: dict) -> float:
    """
    Функция, которая возвращает сумму транзакций в рублях.
    """
    all_sum = 0
    logger.info("Суммируем все рубли и конвертируем доллары в рубли и их тоже суммируем")

    if not isinstance(transaction_list, list):
        logger.error("Передан не список транзакций")
        return 0  # Если передан словарь или другая структура, возвращаем 0

    for i in transaction_list:
        try:
            currency = i["operationAmount"]["currency"]["code"]
            amount = i["operationAmount"]["amount"]

            if currency == "RUB":
                all_sum += float(amount)
            else:
                alternative_summ = convertation_curency(currency, "RUB", float(amount))
                if alternative_summ != "Error":
                    all_sum += float(alternative_summ)
        except (KeyError, TypeError, ValueError) as e:
            logger.warning(f"Ошибка при обработке транзакции: {e}")
            continue

    logger.info(f"Получаем сумму всех транзакций: {all_sum}")
    return all_sum
