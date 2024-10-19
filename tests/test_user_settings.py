import pytest
from src.user_settings import load_user_settings, get_current_price, get_current_stock, add_to_list, settings
import os
import json
from dotenv import load_dotenv
import requests


def test_load_user_settings():
    # Проверяем, что функция возвращает словарь
    settings = load_user_settings()
    assert isinstance(settings, dict), "load_user_settings должен вернуть словарь"

    # Проверяем, что в словаре есть нужные ключи
    expected_keys = {'user_currencies', 'user_stocks'}
    assert set(settings.keys()) >= expected_keys, "Словарь должен содержать ожидаемые ключи"

    # Проверяем, что файл существует
    project_root = '/home/oem/PycharmProjects/curs_project/'
    settings_path = os.path.join(project_root, 'user_settings.json')
    assert os.path.exists(settings_path), f"Файл {settings_path} не найден"


def test_get_current_price():
    price = get_current_price("RUB")

    # Проверяем, что результат - словарь
    assert isinstance(price, dict), "Функция должна вернуть словарь"

    # Проверяем содержимое словаря
    assert 'currency' in price, "'currency' ключ отсутствует"
    assert 'rate' in price, "'rate' ключ отсутствует"
    assert price['currency'] == "RUB", "Неверная валюта"
    assert isinstance(price['rate'], (int, float)), "Рейт должен быть числом"

    # Проверяем, что API работает корректно
    url = f"https://api.exchangerate-api.com/v4/latest/RUB"
    response = requests.get(url)
    assert response.status_code == 200, f"Ошибка при запросе к API. Статус код: {response.status_code}"


def test_get_current_stock():
    stocks = get_current_stock()
    assert isinstance(stocks, list), "get_current_stock должен вернуть список"
    assert all(isinstance(stock, dict) for stock in stocks), "Все элементы списка должны быть словарями"

    # Проверяем, что в каждом словаре есть нужные ключи
    expected_keys = {'symbol', 'price'}
    for stock in stocks:
        assert set(stock.keys()) >= expected_keys, f"Словарь {stock} не содержит ожидаемых ключей"


def test_add_to_list():
    currency_list = add_to_list()
    assert isinstance(currency_list, list), "add_to_list должен вернуть список"
    assert all(isinstance(item, dict) for item in currency_list), "Все элементы списка должны быть словарями"

    # Проверяем, что список содержит данные о валютах
    assert len(currency_list) == len(settings["user_currencies"]), "Несоответствие количества валют"

    # Проверяем, что все элементы списка имеют нужные ключи
    expected_keys = {'currency', 'rate'}
    for item in currency_list:
        assert set(item.keys()) >= expected_keys, f"Элемент {item} не содержит ожидаемых ключей"


# Дополнительный тест для проверки загрузки переменных окружения
def test_load_dotenv():
    load_dotenv()
    assert os.getenv("STOCK_API_KEY") is not None, "API_KEY_2 не загружен из .env файла"
