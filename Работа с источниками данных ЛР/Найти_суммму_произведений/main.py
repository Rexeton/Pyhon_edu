# TODO решите задачу
import json
FILENAME='input.json'
def task() -> float:
    with open(FILENAME, 'r', encoding="utf-8") as f:
        json_f = json.load(f)
    return round(sum(el['score']*el['weight'] for el in json_f),3)

print(task())
