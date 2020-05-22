import json
import csv

# data = {
#     "users": [
#         {"name": "Dominator", "skill": 100, "gold": 99999, "weapons": ['Sword', 'Atomic Laser']},
#         {"name": "Looser", "skill": 1, "gold": -100000, "weapons": [None, 'sword', None]},
#         {"name": "Kirill", "skill": 10, "gold": 6666, "weapons": ['Bomb', 'Laser', None]}
#     ]
# }
#
# with open("example1.json", "w") as f:
#     s = json.dumps(data, indent=3)
#     f.write(s)

users = []
with open('../files/users.csv') as file:
    reader = csv.reader(file)

    # Извлекаем заголовок
    header = next(reader)

    # Итерируемся по данным делая из них словари
    for row in reader:
        users.append(dict(zip(header, row)))

data = {"users":users}

with open("users.json", "w") as file:
    s = json.dumps(data, indent=3)
    file.write(s)

