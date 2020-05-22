import json

with open("../files/example.json", "r") as file:
#    print(file.read())
    users = json.loads(file.read())

users_list = users['users']

for user in users_list:
    print(user)