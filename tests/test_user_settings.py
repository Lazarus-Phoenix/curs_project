import pytest
from src.user_settings import load_user_settings, get_current_price, get_current_stock, add_to_list


def test_load_user_settings():
    settings = load_user_settings()
    assert isinstance(settings, dict), "load_user_settings должен вернуть словарь"


def test_get_current_price():
    price = get_current_price("RUB")

    # Проверяем, что результат - словарь
    assert isinstance(price, dict), "Функция должна вернуть словарь"

    # Проверяем содержимое словаря
    assert 'currency' in price, "'currency' ключ отсутствует"
    assert 'rate' in price, "'rate' ключ отсутствует"
    assert price['currency'] == "RUB", "Неверная валюта"
    assert isinstance(price['rate'], (int, float)), "Рейт должен быть числом"


def test_get_current_stock():
    stocks = get_current_stock()
    assert isinstance(stocks, list), "get_current_stock должен вернуть список"
    assert all(isinstance(stock, dict) for stock in stocks), "Все элементы списка должны быть словарями"

def test_add_to_list():
    currency_list = add_to_list()
    assert isinstance(currency_list, list), "add_to_list должен вернуть список"
    assert all(isinstance(item, dict) for item in currency_list), "Все элементы списка должны быть словарями"
