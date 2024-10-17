import pytest
from src.views import main

@pytest.fixture
def mock_input():
    def mock_input(prompt):
        return "2021-05-20 18:50:27"
    return mock_input

def test_module_is_alive(monkeypatch):
    def mock_input_side_effect(prompt):
        return "2021-05-20 18:50:27"

    monkeypatch.setattr('builtins.input', mock_input_side_effect)

    assert main() is None