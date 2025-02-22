import json

file_path = "C:/Users/wavekitt/PythonProject4/data/operations.json"

with open(file_path) as f:
    data = json.load(f)

print(data)