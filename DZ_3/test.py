import csv
import json


# 1 - Чтение .csv и перевод его в .json

with open('../DZ_3/books.csv', newline='') as file:
    reader = csv.reader(file)

    # Извлекаем заголовок
    header = next(reader)

b = []
# Итерируемся по данным делая из них словари
for book in reader:
        b.append(book)
        print(book)

# 2 - Чтение .json
# with open("../DZ_3/users.json", "r") as file:
#     users = json.loads(file.read())
#
# users_list = users['users']
# for users in users_list:
#     print(users)

# combo_list = b + users_list
# print(combo_list)
