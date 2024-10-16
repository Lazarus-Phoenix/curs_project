# -*- coding: utf-8 -*-
import json
import datetime
from src.utils import get_excel, filtered_cards, filtered_top
from src.user_settings import get_current_price, get_current_stock, settings


def get_greeting():
    """ Функция приветствия , возвращающая сообщение соответствующее реальному времени """
    current_time_now = datetime.datetime.now()

    if 6 <= current_time_now.hour < 12:
        return f"Доброе утро!"
    elif 12 <= current_time_now.hour < 18:
        return f"Добрый день!"
    elif 18 <= current_time_now.hour < 24:
        return f"Добрый вечер!"
    else:
        return f"Доброй ночи"



# def get_greeting(current_time):
#     """Функция приветствия, возвращающая соответствующее сообщение в зависимости от времени суток запроса."""
#     current_time = datetime.datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")
#     current_time = current_time.time()
#     night_end = datetime.time(2, 59, 59)
#     morning_start = datetime.time(5, 0, 0)
#     morning_end = datetime.time(11, 59, 59)
#     evening_start = datetime.time(17, 0, 0)
#     evening_end = datetime.time(23, 59, 59)
#     if current_time <= night_end:
#         return "Доброй ночи!"
#     elif morning_start <= current_time <= morning_end:
#         return "Доброе утро!"
#     elif evening_start <= current_time <= evening_end:
#         return "Добрый вечер!"
#     else:
#         return "Добрый день!"

def get_start_date(current_date):
    """Функция, возвращающая дату начала месяца."""
    return current_date[:8] + "01"

def get_transactions(current_date):
    """Функция, возвращающая транзакции за указанный период."""
    start_date = get_start_date(current_date)
    transactions = get_excel("dict")
    
    # Преобразуем даты в объекты datetime
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d %H:%M:%S")
    
    def safe_parse_date(date_str):
        try:
            return datetime.datetime.strptime(str(date_str), "%d.%m.%Y")
        except ValueError:
            return None
    
    return [t for t in transactions if 
            (date := safe_parse_date(t["Дата платежа"])) is not None and 
            start_date <= date <= current_date]

def generate_json_response(current_date):
    """Главная функция, генерирующая JSON-ответ."""
    transactions = get_transactions(current_date)
    print(f"Количество транзакций: {len(transactions)}")
    
    response = {
        "greeting": get_greeting(),
        "cards": filtered_cards(transactions),
        "top_transactions": filtered_top(transactions),
        "currency_rates": [get_current_price(currency) for currency in settings["user_currencies"]],
        "stock_prices": get_current_stock()
    }

    return json.dumps(response, ensure_ascii=False, indent=4)

# Пример использования
if __name__ == "__main__":
    current_date = "2020-05-20 12:00:00"
    print(generate_json_response(current_date))


