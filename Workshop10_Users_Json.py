import json
with open("users.json") as users:
    data = json.load(users)
    for x in range(5):
        print(data[0]["username"])
        print(data[0]["email"])
        print(data[0]["address"])
        print(data[0]["address"]["street"])
        print(data[0]["address"]["geo"])
        print(data[0]["address"]["geo"]["lat"])