# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f:
        csv_data = csv.DictReader(f,delimiter=',', quotechar=',') # TODO считать содержимое csv файла
        aa= []
        for row in csv_data:
            aa.append(row)
        with open(OUTPUT_FILENAME, 'w', encoding="utf-8") as ff:
            json.dump(aa,ff,indent=4) #json.dumps(1,indent=4)  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
