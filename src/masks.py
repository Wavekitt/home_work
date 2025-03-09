import logging
import os

log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(log_dir, exist_ok=True)
log_file_masks = os.path.join(log_dir, "masks_card_account.log")
logger = logging.getLogger("masks_card_account")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file_masks, "w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    функция, которая маскирует номер карты.
    """
    if len(card_number) == 16:
        masked_card_number = " ".join(
            card_number[i * 4:(i + 1) * 4] for i in range(4)
        ).split(" ")
        masked_card_number[1] = masked_card_number[1].replace(
            masked_card_number[1][2:], "**"
        )
        masked_card_number[2] = masked_card_number[2].replace(
            masked_card_number[2], "****"
        )
        masked_card_number = " ".join(masked_card_number)
        logger.info(f"Замаскировали карту: {masked_card_number}")
        return masked_card_number  # возвращает замаскированный номер карты.
    else:
        logger.error("Неверные данные!")
        return "Неверные данные!"  # возвращает при неверном номере карты


def get_mask_account(account_number: str) -> str:
    """
    функция, которая маскирует номер аккаунта
    """
    if len(account_number) == 20:
        account_number = account_number[-6:]
        account_number = account_number.replace(account_number[:2], "**")
        logger.info(f"Замаскировали номер аккаунта: {account_number}")
        return account_number  # возвращает замаскированный номер аккаунта
    else:
        logger.error("Неверные данные!")
        return "Неверные данные!"  # возвращает при неверном номере аккаунта
