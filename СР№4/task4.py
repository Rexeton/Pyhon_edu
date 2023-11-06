from random import choice


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    count_monets={'Орел': 0,'Решка':0}
    for i in range(count+1):
        rez=choice([EAGLE, TAILS])
        count_monets[rez]+=1  # TODO подсчитать количество выпаданий орлов и решек
    list_freq.append(min(count_monets.values())/max(count_monets.values()))
    # TODO разделить минимальное число среди орлов и решек на максимальное число и сохранить результат

print(list_freq)
