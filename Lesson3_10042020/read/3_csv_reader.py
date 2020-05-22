import csv
from csv import DictReader

with open('../files/users.csv', newline='') as file:
    reader = csv.reader(file)

    # Извлекаем заголовок
    header = next(reader)

    # Итерируемся по данным делая из них словари
    for row in reader:
#        print(row)
#        ziped_data = zip(header,row)
#        print(dict(ziped_data))
       print(dict(zip(header, row)))


# print(100 * "+")
#
#
# with open('../files/users.csv', newline='') as f:
#     reader = DictReader(f)
#
#     # Итерируемся по данным делая из них словари
#     for row in reader:
#         print(row)