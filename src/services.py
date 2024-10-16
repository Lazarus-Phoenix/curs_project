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
        print(f"Возникла ошибка {e}")
        logger.error(f"Возникла ошибка {e}")
        return ""


testing = get_excel("dict")
# print(search_transaction_by_mobile_phone(testing))



# import json
# import os
# import re
# import pandas as pd
# from typing import List, Dict
# from datetime import datetime
# import logging
#
# from src.constants import DATE_FORMAT
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler = logging.StreamHandler()
# handler.setFormatter(formatter)
# logger.addHandler(handler)
#
# def get_operations_dict(filepath: str) -> List[Dict]:
#     logger.debug(f"Чтение файла: {filepath}")
#
#     # Определяем полный путь к файлу
#     root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     data_dir = os.path.join(root_dir, "data")
#     full_filepath = os.path.join(data_dir, "operations.xlsx")
#
#     # Проверяем существование файла
#     if not os.path.exists(full_filepath):
#         raise FileNotFoundError(f"Файл {full_filepath} не ��айден")
#
#     try:
#         operations = pd.read_excel(full_filepath)
#         logger.debug(f"Файл успешно прочитан. Количество строк: {len(operations)}")
#
#         # Преобразуем дату из формата "DD.MM.YYYY HH:MM:SS" в нужный формат
#         operations['Дата операции'] = operations['Дата операции'].apply(lambda x: datetime.strptime(str(x), "%d.%m.%Y %H:%M:%S").strftime(DATE_FORMAT))
#
#         return operations.to_dict('records')
#     except Exception as e:
#         logger.error(f"Ошибка при чтении файла {full_filepath}: {str(e)}")
#         raise
#
#
# def find_string(search_bar: str, data: List[Dict]) -> str:
#     """
#     функция поиска операций с определенными словами в описании
#     """
#     result = []
#     pattern = re.compile(search_bar, re.IGNORECASE)
#     for operation in data:
#         if pattern.search(str(operation["Категория"])):
#             result.append(operation)
#
#     return json.dumps(result, ensure_ascii=False)
#
#
# # print(find_string(os.path.join("..", "data", "operations.xls"), "Перево��ы"))
# # print(get_operations_dict(os.path.join("..", "data", "operations.xls"))
