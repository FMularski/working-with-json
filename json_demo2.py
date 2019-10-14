import json

with open('states.json') as file:
    data = json.load(file)

print(data)