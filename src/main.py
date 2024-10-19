# -*- coding: utf-8 -*-
import logging

from src.json_generator import generate_json_response
from src.logger import setup_logger
from src.reports import spending_by_category
from src.services import search_transaction_by_mobile_phone, testing
from src.utils import get_excel


def main():
    """Итоговая функция, которая запускает  в качестве DEMO весь функционал программы"""

    logger = setup_logger("main", "logs/main.log")

    logger.info("Программа запущена")
    print("\nПривет!\n Добро пожаловать в программу работы с банковскими транзакциями.\n")
    print("Выберите необходимый пункт меню:\n")
    print("1. Добро пожаловать в API для главной страницы.")
    print("2. Поиско транзакций с указанным телефонным номером.")
    print("3. Получить информацию о тратах по категории с трёхмесячной выборкой по дате.")

    choice = input("\nВведите пункт вашего поиска--->: ")
    if choice not in ["1", "2", "3"]:
        return "Неверный ввод. Пожалуйста, выберите пункт 1, 2 или 3."
    if choice == "1":
        print("Добро пожаловать на главную страницу")
        print("Сейчас вам вы можете произвести поиск транзакции по дате")
        print("Выбирайте для  например из")
        print("2021-12-26 20:39:43")
        print("2019-07-26 16:09:05")
        print("2018-03-30 13:35:48")
        current_date = input("Введите дату и время в формате YYYY-MM-DD HH:MM:SS: ")
        print(generate_json_response(current_date))
        return
    elif choice == "2":
        print("Поиск транзакций с указанными телефонными номерами")
        print(search_transaction_by_mobile_phone(testing))
        return
    else:
        print("Информация о тратах по категории")
        print("Выбирайте из диапазона от 01.04.2018 до 31.12.2021")

        period_data = input("Введите от какой даты выборка за 3 месяца: ")
        category_name = input("Введите на выбор(Фасфуд, ЖКХ, Связь, Транспорт): ")

        print(*spending_by_category(get_excel("dataframe"), category_name, period_data), sep="\n")
        return


if __name__ == "__main__":
    main()
