# with open("../files/example.txt", "r", encoding="utf-8") as file:
#     print(file.read())

# print("\n", 20 * "=", "\n")
#
with open("../files/example.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line, end='')