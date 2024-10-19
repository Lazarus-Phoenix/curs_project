import json

import pytest
from src.services import search_transaction_by_mobile_phone, testing
from src.utils import get_excel


def test_search_transaction_by_mobile_phone():
    # Предполагаем, что функция search_transaction_by_mobile_phone() всегда возвращает JSON строку
    actual_result = search_transaction_by_mobile_phone(testing)

    # Проверяем, что функция не вызывает исключений
    assert isinstance(actual_result, str), "Функция должна вернуть строку"

    # Проверяем, что функция не пустая
    # assert len(actual_result) > 0, "Функция должна вернуть непустую строку"

    # Проверяем, что функция не None
    assert actual_result is not None, "Функция не может вернуть None"

def test_empty_result():
    empty_transactions = [{"Описание": ""}]
    actual_result = search_transaction_by_mobile_phone(empty_transactions)
    assert actual_result == json.dumps([], ensure_ascii=False, indent=4)

# def test_testing_function():
#     result = get_excel("dict")
#     assert isinstance(result, list)
#     assert len(result) > 0