import json
# data = json.loads()
with open("C:/Users/deepi/Desktop/Telcolearn/Day 14/mtcars.json") as car:
    data =json.load(car)

# print(data[0]["model"])

for car in data:
    print(car["model"])

# models = [car["model"] for car in data]
# print(models)
