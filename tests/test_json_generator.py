# test_json_generator.py

import pytest
from src.json_generator import get_transactions, generate_json_response
from unittest.mock import patch
import datetime


@patch('src.utils.get_excel')
def test_get_transactions(mock_get_excel):
    mock_get_excel.return_value = [
        {"Дата платежа": "150123", "Сумма операции": 100},
        {"Дата платежа": "150124", "Сумма операции": 200}
    ]

    result = get_transactions("2023-01-15 12:00:00")
    assert isinstance(result, list)
    assert len(result) == 0


@patch('src.utils.get_excel')
@patch('src.json_generator.get_transactions')
def test_generate_json_response(mock_get_transactions, mock_get_excel):
    mock_get_transactions.return_value = [
        {"Дата платежа": "150123", "Сумма операции": 100},
        {"Дата платежа": "150124", "Сумма операции": 200}
    ]

    result = generate_json_response("2023-01-15 12:00:00")
    assert isinstance(result, str)
    assert "greeting" in result
    assert "cards" in result
    assert "top_transactions" in result


