def find_common_participants(participants_first_group, participants_second_group, delimiter=','):
    # Разделение строк по указанному разделителю (по умолчанию - запятая)
    first_group = participants_first_group.split(delimiter)
    second_group = participants_second_group.split(delimiter)

    # Преобразование списков в множества для нахождения пересечения (общих участников)
    common_participants = list(set(first_group) & set(second_group))

    # Сортировка полученного списка общих участников в алфавитном порядке
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверка работы функции с разделителем, отличным от запятой (|)
result = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print("Общие участники:", result)