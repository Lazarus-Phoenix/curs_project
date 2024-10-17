# -*- coding: utf-8 -*-
import functools
from datetime import datetime
from typing import Optional
from src.logger import setup_logger
import pandas as pd
from dateutil.relativedelta import relativedelta


logger = setup_logger("reports", "logs/reports.log")


def report_decorator(filename=None):
    """Декоратор для записи в файл"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, "a") as f:
                f.write(f"{result}\n")
            logger.info(f"Записан результат работы функции {func}")
            return result
        logger.info(f"Записан результат работы функции {func}")
        return wrapper

    return decorator


def date_three_months_ago(date):
    """Функция получает три последних месяца"""
    date_format = "%d.%m.%Y"
    date = datetime.strptime(date, date_format)
    new_date = date - relativedelta(months=3)
    logger.info(f"Траты за последние три месяца от {date}")
    return new_date.strftime(date_format)


def date_now():
    """Функция получает текущую дату"""
    now = datetime.now()
    formatted_date = now.strftime("%d.%m.2021")
    return formatted_date


@report_decorator("report.txt")
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = date_now()):
    """Функция возвращает траты по заданным дате выборки в 3 месяца и категории
    Для API по умолчанию стоит настоящее время, но при тестовой таблице xlsx
    c данными о транзакциях эры кайнозой это приведёт к исключению
    """
    if date is None:
        return []
    # выборка трёхмесячного периода
    date_format = "%d.%m.%Y"
    end_date = datetime.strptime(date, date_format)
    start_date = end_date - relativedelta(months=3)

    current_transactions = []
    for index, transaction in transactions.iterrows():
        if not isinstance(transaction["Дата платежа"], str):
            continue
        transaction_date = datetime.strptime(transaction["Дата платежа"], date_format)
        if transaction["Категория"] == category and start_date <= transaction_date <= end_date:
            current_transactions.append(transaction.to_dict())
    logger.info(f"Траты за последние три месяца от {date} по категории {category}")
    return current_transactions


