from src.json_generator import generate_json_response


def main():
    current_date = input("Введите дату и время в формате YYYY-MM-DD HH:MM:SS: ")
    print(generate_json_response(current_date))


if __name__ == "__main__":
    main()
