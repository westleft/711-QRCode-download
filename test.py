import json

file = open('data.json', 'r', encoding="utf-8")

data = json.loads(file.read())

# for index, item in enumerate(data['sender']):
print(data['sender'])

