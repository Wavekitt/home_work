import json
from src.external_api import convertation_curency
import logging


logger = logging.getLogger("utils_log")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils_log.log", "w", encoding="utf-8")
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
    for i in transaction_list:
        try:
            currency = i["operationAmount"]["currency"]["code"]
            amount = i["operationAmount"]["amount"]
            if currency == "RUB":
                all_sum += float(amount)
            else:
                alternative_summ = convertation_curency(currency, "RUB", amount)
                if not alternative_summ == "Error":
                    all_sum += float(alternative_summ)
        except KeyError:
            logger.warning("превышен результат запросов по api ключу")
            continue
    logger.info(f"получаем сумму всех транзакций {all_sum}")
    return all_sum


print(summ_transactions(transaction_list=list_return(file_path)))
