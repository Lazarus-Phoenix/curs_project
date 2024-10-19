import pytest
from unittest.mock import patch
from io import StringIO
import sys
from src.main import main

def test_main_function():
    # Создаем мок для input
    mock_input = ["1", "2021-05-20 18:50:27", "2", "2021-05-20 18:50:27", "3", "2021-05-20 18:50:27", "Фасфуд", "2021-05-20", "4"]

    # Создаем мок для print
    capturedOutput = StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                   # Redirect stdout

    # Заменяем реальный input на наш мок
    with patch('builtins.input', side_effect=mock_input):
        main()

    # Возвращаем stdout обратно
    sys.stdout = sys.__stdout__                   # Reset redirect

    # Получаем вывод функции
    actual_output = capturedOutput.getvalue()

    # Проверяем, что функция вернула строку
    assert isinstance(actual_output, str)
    assert len(actual_output) > 0


    # Проверяем, что функция обработала все вводы
    assert mock_input == ['1',
                          '2021-05-20 18:50:27',
                          '2',
                          '2021-05-20 18:50:27',
                          '3',
                          '2021-05-20 18:50:27',
                          'Фасфуд',
                          '2021-05-20',
                          '4']

    # Проверяем вывод для каждого случая
    assert "Неверный ввод. Пожалуйста, выберите пункт 1, 2 или 3." not in actual_output, "Функция должна обработать неверный ввод"

    # Проверяем вывод для случая 1
    assert "Добро пожаловать на главную страницу" in actual_output
    assert "Сейчас вам вы можете произвести поиск транзакции по дате" in actual_output
    assert "2021-12-26 20:39:43" in actual_output
    assert "2019-07-26 16:09:05" in actual_output
    assert "2018-03-30 13:35:48" in actual_output


