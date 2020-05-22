some_file = open("../files/example.txt", "r", encoding="utf-8")

# # Читаем кол-во байт
# print(some_file.read(7))
#
# # Читаем строку
print(some_file.readline())
#
# # Построчно массив
# print(some_file.readlines(), "\n")

# for line in some_file.readlines():
#     print(line)
# Всё что осталось
print(some_file.read())

some_file.close()