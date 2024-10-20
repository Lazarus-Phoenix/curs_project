import json

import pytest
from unittest.mock import patch, MagicMock
from src.user_settings import (
    load_user_settings, get_current_price, get_current_stock, add_to_list, settings
)

@pytest.fixture
def mock_requests_get():
    with patch('requests.get') as mock_get:
        yield mock_get

def test_load_user_settings(tmp_path):
    # Создаем временный файл с тестовыми данными
    test_file = tmp_path / "user_settings.json"
    test_data = {
        "user_currencies": ["USD", "EUR"],
        "user_stocks": ["AAPL", "GOOG"]
    }
    test_file.write_text(json.dumps(test_data))

    # Переопределяем путь к файлу
    with patch('os.path.join', return_value=str(test_file)):
        loaded_settings = load_user_settings()

    assert isinstance(loaded_settings, dict)
    assert set(loaded_settings.keys()) >= {'user_currencies', 'user_stocks'}
    assert loaded_settings['user_currencies'] == test_data['user_currencies']
    assert loaded_settings['user_stocks'] == test_data['user_stocks']

def test_get_current_price(mock_requests_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "rates": {"RUB": 1.0}
    }
    mock_requests_get.return_value = mock_response

    price = get_current_price("RUB")

    assert isinstance(price, dict)
    assert price['currency'] == "RUB"


def test_get_current_stock(mock_requests_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "symbol": ["AAPL", "GOOG"],
        "price": [100.0, 1500.0]
    }
    mock_requests_get.return_value = mock_response

    stocks = get_current_stock()

    assert isinstance(stocks, list)
    assert len(stocks) == 5
    assert all(isinstance(stock, dict) for stock in stocks)

def test_add_to_list(mock_requests_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "rates": {"USD": 60.0, "EUR": 70.0}
    }
    mock_requests_get.return_value = mock_response

    currency_list = add_to_list()

    assert isinstance(currency_list, list)
    assert len(currency_list) == 2
    assert all(isinstance(item, dict) for item in currency_list)

