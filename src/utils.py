# -*- coding: utf-8 -*-
import pandas as pd
from src.logger import setup_logger

logger = setup_logger("utils", "logs/utils.log")

def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Возникла ошибка: {str(e)}")
            # Здесь можно добавить дополнительную логику обработки ошибок
    return wrapper

def read_excel(file_path):
    return pd.read_excel(file_path)

@handle_error
def get_excel(formatting):
    """Читает файл и форматирует в дф или словарь"""
    get_excel_file = pd.read_excel("../data/operations.xlsx")
    logger.info("файл перекодирован в список словарей")
    if formatting == "dataframe":
        return get_excel_file
    elif formatting == "dict":
        return get_excel_file.to_dict(orient="records")
    else:
        logger.error("Возникла ошибка")
        raise ValueError("Invalid format specified. Use 'dataframe' or 'dict'.")


# print(get_excel('dataframe'))

@handle_error
def generate_json(current_date, transactions):
    """Функция, возвращающая отфильтрованные по дате транзакции"""
    current_transactions = []
    for transaction in transactions:
        if (
            str(transaction["Дата платежа"])[2:10] == current_date[2:10]
            and str(transaction["Дата платежа"])[:2] <= current_date[:2]
        ):
            current_transactions.append(transaction)
    return current_transactions

@handle_error
def filtered_cards(transactions):
    """Функция, возвращающая правильный список карт
    и положительный кэшбек , потому что отнимать кэшбэк это оксюморон.
    """
    cards = []
    for transaction in transactions:
        card = {
            "last_digit": transaction["Номер карты"],
            "total_spent": transaction["Сумма операции"],
            "cashback": round(transaction["Сумма операции"] * 0.01, 2) if transaction["Сумма операции"] > 0 else 0
            # "cashback": round(transaction["Сумма операции"] / 100, 2),
        }
        cards.append(card)
    return cards


@handle_error
def filtered_top(transactions):
    """Функция, возвращающая топ 3 транзакций по платежам"""
    sort_current_transactions = sorted(transactions, reverse=True, key=lambda x: abs(x["Сумма платежа"]),)
    top_list = []
    for transaction in sort_current_transactions:
        top = {
            "date": transaction["Дата платежа"],
            "amount": abs(transaction["Сумма платежа"]),
            "category": transaction["Категория"],
            "description": transaction["Описание"],
        }
        top_list.append(top)
        if len(top_list) == 3:
            break
    return top_list


