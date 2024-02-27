import json
with open('./example.json') as file:
    dct = json.load(file)

print(dct)