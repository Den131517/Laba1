import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Считать содержимое CSV файла
    data = []
    with open(INPUT_FILENAME, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Считываем заголовок

        for row in csv_reader:
            # Создаем словарь, используя заголовок как ключи
            row_dict = {header[i]: row[i] for i in range(len(header))}
            data.append(row_dict)

    # Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    # Выводим содержимое JSON файла
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
