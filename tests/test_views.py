import json
import unittest
from unittest import TestCase

from src.json_generator import generate_json_response


class TestJsonResponse(TestCase):
    def setUp(self):
        self.result = json.loads(generate_json_response("2018-03-30 13:35:48"))

    def test_response_structure(self):
        self.assertIn("greeting", self.result)
        self.assertIn("cards", self.result)
        self.assertIn("top_transactions", self.result)
        self.assertIn("currency_rates", self.result)
        self.assertIn("stock_prices", self.result)

    def test_cards_length(self):
        self.assertEqual(len(self.result["cards"]), 131)

    def test_top_transactions(self):
        self.assertEqual(len(self.result["top_transactions"]), 3)

    def test_currency_rates(self):
        self.assertEqual(len(self.result["currency_rates"]), 2)
        self.assertEqual(self.result["currency_rates"][0]["currency"], "USD")
        self.assertEqual(self.result["currency_rates"][0]["rate"], 96.83)
        self.assertEqual(self.result["currency_rates"][1]["currency"], "EUR")
        self.assertEqual(self.result["currency_rates"][1]["rate"], 104.93)

    def test_stock_prices(self):
        self.assertEqual(len(self.result["stock_prices"]), 5)
        self.assertIn("AMZN", [s["stock"] for s in self.result["stock_prices"]])
        self.assertIn("TSLA", [s["stock"] for s in self.result["stock_prices"]])
        self.assertIn("AAPL", [s["stock"] for s in self.result["stock_prices"]])
        self.assertIn("GOOGL", [s["stock"] for s in self.result["stock_prices"]])
        self.assertIn("MSFT", [s["stock"] for s in self.result["stock_prices"]])

if __name__ == '__main__':
    unittest.main()


# import pytest
# from src.json_generator import generate_json_response
# from unittest.mock import patch
# from io import StringIO
# import sys
#
# from src.views import main
#
#
# class InputMocker:
#     def __init__(self, inputs):
#         self.inputs = inputs
#         self.index = 0
#
#     def __call__(self, prompt):
#         if self.index < len(self.inputs):
#             result = self.inputs[self.index]
#             self.index += 1
#             return result
#         else:
#             raise IndexError("No more inputs available")
#
#     def reset(self):
#         self.index = 0
#
# @pytest.fixture
# def mock_input():
#     return InputMocker(["2021-05-20 18:50:27"])
#
# def test_views_main_function(mock_input):
#     with patch('builtins.input', mock_input):
#         capturedOutput = StringIO()
#         sys.stdout = capturedOutput
#         main()
#         sys.stdout = sys.__stdout__
#         actual_output = capturedOutput.getvalue()
#
#     assert isinstance(actual_output, str)
#     assert len(actual_output) > 0
#
#     greeting_options = ["Доброе утро!", "Добрый день!", "Добрый вечер!", "Доброй ночи!"]
#     assert any(option in actual_output for option in greeting_options), \
#         f"Отсутствует ожидаемое приветствие. Возможные варианты: {greeting_options}"
