import json

def task() -> float:
    result = 0
    with open("input.json", "r") as fh:
        data = json.load(fh)
        for i in data:
            result += i["score"] * i["weight"]
    return round(result, 3)

print(task())
