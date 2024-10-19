import pytest
from src.reports import spending_by_category
import pandas as pd
from unittest.mock import patch, Mock
from datetime import datetime


@pytest.fixture
def mock_excel_data():
    data = {
        "Дата платежа": ["01.05.2021", "02.06.2021", "03.07.2021"],
        "Категория": ["Продукты", "Услуги", "Продукты"],
        "Сумма": [1000, 2000, 1500]
    }
    df = pd.DataFrame(data)
    return df


@pytest.fixture
def mock_date_three_months_ago():
    def mock_func(date):
        return datetime.strptime("01.04.2021", "%d.%m.%Y").strftime("%d.%m.%Y")

    return mock_func


@pytest.fixture
def mock_date_now():
    def mock_func():
        return "31.12.2021"

    return mock_func


def test_spending_by_category(mock_excel_data, mock_date_three_months_ago, mock_date_now):
    # Создаем мокированную версию read_excel
    mock_read_excel = lambda: mock_excel_data

    # Заменяем реальную функцию на мокированную
    with patch('src.utils.read_excel', side_effect=mock_read_excel), \
            patch('src.reports.date_three_months_ago', new=mock_date_three_months_ago), \
            patch('src.reports.date_now', new=mock_date_now):
        result = spending_by_category(mock_excel_data, "Продукты")

        assert len(result) == 0



    # Тест для случая, когда дата не указана явно
    result = spending_by_category(mock_excel_data, "Продукты", None)
    assert not result

    # Тест для случая, когда выбрано неверное имя категории
    result = spending_by_category(mock_excel_data, "Неверная категория")
    assert not result



# Предполагается, что у вас есть имплементация logger
mock_logger = Mock()


import pytest
from src.reports import date_three_months_ago
from datetime import datetime
from dateutil.relativedelta import relativedelta

def test_date_three_months_ago():
    # Тест с текущей датой
    today = datetime.now().strftime("%d.%m.%Y")
    result = date_three_months_ago(today)
    expected = (datetime.strptime(today, "%d.%m.%Y") - relativedelta(months=3)).strftime("%d.%m.%Y")
    assert result == expected

def test_date_three_months_ago_edge_case():
    # Тест на границе года
    date = "31.12.2022"
    result = date_three_months_ago(date)
    expected = "30.09.2022"
    assert result == expected

def test_date_three_months_ago_leap_year():
    # Тест для високосного года
    date = "29.02.2020"
    result = date_three_months_ago(date)
    expected = "29.11.2019"
    assert result == expected

def test_date_three_months_ago_invalid_format():
    # Тест с некорректным форматом даты
    with pytest.raises(ValueError):
        date_three_months_ago("invalid-date")

def test_date_three_months_ago_future_date():
    # Тест с будущей датой
    future_date = (datetime.now() + relativedelta(years=1)).strftime("%d.%m.%Y")
    result = date_three_months_ago(future_date)
    expected = (datetime.strptime(future_date, "%d.%m.%Y") - relativedelta(months=3)).strftime("%d.%m.%Y")
    assert result == expected

