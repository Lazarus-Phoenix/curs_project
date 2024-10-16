import os
import requests
from dotenv import load_dotenv
import json

# Загружаем переменные окружения из .env файла
load_dotenv()

# Актуальный API ключ
API_KEY_2 = os.getenv("STOCK_API_KEY")


def load_user_settings():
    project_root = '/home/oem/PycharmProjects/curs_project/'
    settings_path = os.path.join(project_root, 'user_settings.json')

    try:
        with open(settings_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл user_settings.json не найден в {project_root}")
        return {}
    except json.JSONDecodeError:
        print(f"Ошибка при декодировании JSON в {settings_path}")
        return {}


# Загрузка настроек при инициализации модуля
settings = load_user_settings()

# Настройки пользователей
# settings = {
#     "user_currencies": ["USD", "EUR"],
#     "user_stocks": ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
# }

def get_current_price(currency=None):
    '''������� ���������� �������� �� ���������������� �������� ������'''
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
    '''������� ���������� ����� ��� � ������� � �������� ���������� ��������� �����'''
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
    '''������� ��������� � ������ �������� �� ���������������� �������� ������'''
    currency_list = []
    for currency in settings["user_currencies"]:
        currency_list.append(get_current_price(currency))
    return currency_list
