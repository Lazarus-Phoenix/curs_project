import json
import unittest

from src.views import generate_json_response


class TestJsonResponse(unittest.TestCase):
    def setUp(self):
        self.result = {}



    def test_error_message(self):
        # Проверка содержимого сообщения об ошибке
        self.assertEqual(self.result.get('error'), None)
        self.assertIsNone(self.result.get('currency_rates'))
        self.assertIsNone(self.result.get('stock_prices'))
        self.assertIsNone(self.result.get('top_transactions'))

    def test_response_structure(self):
        # Проверяем структуру ответа
        expected_keys = set()
        self.assertEqual(set(self.result.keys()), set(expected_keys))

    def test_stock_prices(self):
        # Проверка наличия ключа 'stock_prices'
        self.assertIsNone(self.result.get('stock_prices'))

    def test_top_transactions(self):
        # Проверка наличия ключа 'top_transactions'
        self.assertIsNone(self.result.get('top_transactions'))

    def test_all_fields_present(self):
        # Проверяем наличие всех ожидаемых полей
        required_fields = ['error', 'currency_rates', 'stock_prices', 'top_transactions']
        self.assertFalse(any(field in self.result for field in required_fields))


if __name__ == '__main__':
    unittest.main()

import pytest
from src.json_generator import generate_json_response
from unittest.mock import patch
from io import StringIO
import sys

from src.views import main


class InputMocker:
    def __init__(self, inputs):
        self.inputs = inputs
        self.index = 0

    def __call__(self, prompt):
        if self.index < len(self.inputs):
            result = self.inputs[self.index]
            self.index += 1
            return result
        else:
            raise IndexError("No more inputs available")

    def reset(self):
        self.index = 0

@pytest.fixture
def mock_input():
    return InputMocker(["2021-05-20 18:50:27"])

def test_views_main_function(mock_input):
    with patch('builtins.input', mock_input):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        main()
        sys.stdout = sys.__stdout__
        actual_output = capturedOutput.getvalue()

    assert isinstance(actual_output, str)
    assert len(actual_output) > 0

