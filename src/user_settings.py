import os
import requests
from dotenv import load_dotenv
import json

from src.logger import setup_logger

# Загружаем переменные окружения из .env файла
load_dotenv()

# Актуальный API ключ
API_KEY_2 = os.getenv("STOCK_API_KEY")

logger = setup_logger("user_settings", "logs/user_settings.log")

def load_user_settings():
    """
    Загружает настройки пользователя из файла user_settings.json.

    Функция пытается открыть файл user_settings.json в корневой директории проекта,
    если файл не найден, то возвращает пустой словарь. Если возникает ошибка при чтении
    JSON, также возвращается пустой словарь.

    Возвращает:
        dict: Словарь с настройками пользователя или пустой словарь в случае ошибок.
    """
    logger.debug("Начало загрузки настроек пользователя")

    project_root = '/home/oem/PycharmProjects/curs_project/'
    settings_path = os.path.join(project_root, 'user_settings.json')

    try:
        with open(settings_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Файл user_settings.json не найден в {project_root}")
        return {}
    except json.JSONDecodeError:
        logger.error(f"Ошибка при декодировании JSON в {settings_path}")
        return {}

logger.info("Настройки пользователя успешно загружены")

# Загрузка настроек при инициализации модуля
settings = load_user_settings()

def get_current_price(currency=None):
    """
    Получает текущий курс валюты.

    Args:
        currency (str): Код валюты для получения курса (например, USD).

    Returns:
        list: Список словарей с информацией о курсе валюты, если currency указан;
              пустой список, если currency не указан.

    Raises:
        Exception: Если произошла ошибка при запросе к API.
    """
    logger.debug(f"Получение курса валюты: {currency}")

    if currency is None:
        return []
    
    url = f"https://api.exchangerate-api.com/v4/latest/{currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch exchange rate. Status code: {response.status_code}")
    
    data = response.json()
    rate = data['rates']['RUB']
    return {"currency": currency, "rate": rate}

def get_current_stock():
    """
    Получает актуальные данные о ценах акций пользовательских бумаг.

    Возвращает:
        list: Список словарей с информацией о ценах акций.
    """
    url = f"https://financialmodelingprep.com/api/v3/stock/list?apikey={API_KEY_2}"
    payload = {}
    response = requests.request("GET", url, data=payload)
    result = response.json()
    currency_stock = []
    for stock in result:
        for my_stock in settings["user_stocks"]:
            if stock["symbol"] == my_stock:
                currency_stock.append({"stock": stock["symbol"], "price": stock["price"]})
    return currency_stock
def add_to_list():
    """
    Добавляет актуальные курсы валют в список.

    Возвращает:
        list: Список словарей с актуальными курсами валют.
    """
    logger.debug("Добавление актуальных курсов валют в список")
    
    currency_list = []
    for currency in settings["user_currencies"]:
        currency_list.append(get_current_price(currency))
    return currency_list
