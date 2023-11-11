import json


def task() -> float:
    # Загрузка данных из JSON файла
    with open('input.json', 'r') as file:
        data = json.load(file)

    # Вычисление суммы произведений "score" * "weight"
    total_sum = sum(entry["score"] * entry["weight"] for entry in data)

    # Округление до 3 знаков после запятой
    rounded_sum = round(total_sum, 3)

    return rounded_sum


print(task())
