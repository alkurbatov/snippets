import json

data = {"a": 1, "b": [1, 2, 3], "c": "xxx"}
print(json.dumps(data, indent=4))
