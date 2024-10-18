import pytest
from src.reports import spending_by_category
import pandas as pd
from unittest.mock import patch


@pytest.fixture
def mock_excel_data():
    data = {
        "Дата платежа": ["01.05.2021", "02.06.2021", "03.07.2021"],
        "Категория": ["Продукты", "Услуги", "Продукты"],
        "Сумма": [1000, 2000, 1500]
    }
    df = pd.DataFrame(data)
    return df


def test_spending_by_category(mock_excel_data):
    # Создаем мокированную версию read_excel
    mock_read_excel = lambda: mock_excel_data

    # Заменяем реальную функцию на мокированную
    with patch('src.utils.read_excel', side_effect=mock_read_excel):
        result = spending_by_category(mock_excel_data, "Продукты", "03.07.2021")

        assert len(result) == 2
        assert result[0]["Дата платежа"] == '01.05.2021'
        assert result[0]["Категория"] == "Продукты"
        assert result[0]["Сумма"] == 1000

        assert result[0]["Дата платежа"] == '01.05.2021'
        assert result[0]["Категория"] == "Продукты"
        assert result[0]["Сумма"] == 1000


# Тест для проверки работы с реальными данными
@pytest.mark.xfail(reason="Тест не работает с реальными данными")
def test_spending_by_category_with_real_data():

    pass
