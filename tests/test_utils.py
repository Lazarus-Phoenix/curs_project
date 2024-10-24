import pandas as pd
import pytest
from src.utils import (
    read_excel,
    get_excel,
    generate_json,
    filtered_cards,
    filtered_top
)

@pytest.fixture
def mock_transactions():
    return [
        {
            "Номер карты": "1234",
            "Сумма операции": 100,
            "Дата платежа": "2023-05-15"
        },
        {
            "Номер карты": "5678",
            "Сумма операции": -50,
            "Дата платежа": "2023-05-16"
        },
        {
            "Номер карты": "9012",
            "Сумма операции": 150,
            "Дата платежа": "2023-05-17"
        }
    ]

def test_read_excel(tmp_path):
    file_path = tmp_path / "test.xlsx"
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    df.to_excel(file_path, index=False)
    assert read_excel(str(file_path)).equals(df)

def test_get_excel(mock_transactions):
    result = get_excel("dataframe")
    assert len(result) == 0
    result = get_excel("dict")
    assert isinstance(result, list)
    assert len(result) == 0
    assert all(isinstance(item, dict) for item in result)

def test_generate_json(mock_transactions):
    current_date = "2023-05-15"
    result = generate_json(current_date, mock_transactions)
    assert len(result) == 1
    assert result[0]["Номер карты"] == "1234"

def test_filtered_cards(mock_transactions):
    result = filtered_cards(mock_transactions)
    assert len(result) == 3
    assert result[0]["last_digit"] == "1234"
    assert result[1]["last_digit"] == "5678"
    assert result[2]["last_digit"] == '9012'


def test_filtered_cards_with_negative_sum(mock_transactions):
    negative_sum_transaction = {
        "Номер карты": "1111",
        "Сумма операции": -75,
        "Дата платежа": "2023-05-18"
    }
    mock_transactions.append(negative_sum_transaction)
    result = filtered_cards(mock_transactions)
    assert len(result) == 4
    assert result[3]["last_digit"] == '1111'

def test_read_excel_with_error(tmp_path):
    file_path = tmp_path / "invalid_file.xlsx"
    open(file_path, 'w').close()
    with pytest.raises(Exception):
        read_excel(str(file_path))
