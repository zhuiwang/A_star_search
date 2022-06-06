
import json

with open('./map.json', 'r') as f:
    data = json.loads(f)

print(data)

# for key, value in data.items():
#     print(key, value)