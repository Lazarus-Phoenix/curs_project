

# Проект "Приложение для анализа транзакций"

## Использование

Демка функционирования и работы предоставлямого API функционала при запуске модуля src/views.py.

## Функционал

В проекте реализованы следующие основные модули:

### Модуль services
- Реализован поиск по телефонным номерам в транзакциях

### Модуль reports
- Генерация отчетов о тратах по категориям
- Выборка данных за трехмесячный период по указанной дате

### Модуль utils
- Все вспомогательные функции проекта

### Модуль views
- Функции для подготовки данных для вывода на главной странице

## Логирование

В проекте реализована система логирования:
- Запись логов в файлы находится в пакете `src/logs`
- Логи содержат информацию о работе модулей и ошибках в процессе обработки

## Тестирование

- Код в модульных пакетах `src/` покрыт тестами
- Для запуска тестов используйте команду `pytest`
- Покрытие тестами составляет 83%
- Для проверки покрытия тестами используйте команду `pytest --cov`

## Структура проекта
markdown curs_project/ 
├── src/ 
│ ├── init.py 
│ ├── main.py 
│ ├── services.py 
│ ├── reports.py 
│ ├── utils.py 
│ ├── views.py  <---API для страницы "Главная"
│ └── logger.py 
├── tests/ 
│ ├── test_views.py 
│ ├── test_json_generator.py 
│ ├── test_user_settings.py 
│ ├── test_utils.py 
│ └── test_reports.py 
├── data/ 
│ └── operations.xlsx 
├── logs/
└── README.md


## Зависимости

Для корректной работы проекта необходимы следующие зависимости:

- pandas
- pytest
- python-dotenv
- requests
- dateutil

Убедитесь, что все эти библиотеки установлены перед запуском проекта.

## Запуск проекта

1. Клонировать репозиторий
2. Создать виртуальное окружение и активировать его
3. Установить зависимости: `pip install -r requirements.txt`
4. Запустить основной скрипт: `python src/views.py`

## API Документация

Доступна в формате личного повествования бывалого кодера который 
 отродясь не кодил, да кааак только начал , успев всего по одному разу прочесть 
матчасть. 
 Аллилуйя братья и сестры ,-Аллилуйя, вы присутствовали при истинном проявлении чуда!

## Авторы

[Lazarus_Phoenix] 

## Лицензия

Этот проект распространяется под лицензией MIT License. Подробнее см. в файле LICENSE.

## Благодарности

Спасибо за использование нашего приложения для анализа транзакций!!!
Следите за нашим творчеством,- мы вас не разочаруем. 