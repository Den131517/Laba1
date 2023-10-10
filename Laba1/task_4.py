users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dictionary = {"Общее количество": 0, "Уникальные посещения": 0}
dictionary["Общее количество"] = len(users)
unique_users = len(set(users))
dictionary["Уникальные посещения"] = unique_users

print(dictionary)
