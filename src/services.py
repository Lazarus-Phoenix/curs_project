import json
import re
from typing import Dict, List
from src.logger import setup_logger
from src.utils import get_excel

logger = setup_logger("services", "logs/services.log")


def search_transaction_by_mobile_phone(transactions: List[Dict]) -> str:
    """Функция возвращает транзакции в описании которых есть мобильный номер"""
    try:
        mobile_pattern = re.compile(r"\+\d{1,4}")
        found_transactions = []
        for transaction in transactions:
            description = transaction.get("Описание", "")
            if mobile_pattern.search(description):
                found_transactions.append(transaction)
        logger.info("Выполнен поиск по транзакциям с номером телефона")
        return json.dumps(found_transactions, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Возникла ошибка  в поиске с номером телефона {e}")
        logger.error(f"Возникла ошибка  в поиске с номером телефона {e}")
        return ""


testing = get_excel("dict")

if __name__ == "__main__":
    print(search_transaction_by_mobile_phone(testing))


