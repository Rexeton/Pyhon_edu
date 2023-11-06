list_ = [4, -1, 10, -1, 3, 3, -1, 8, 6, 9]

# предположим, что первый элемент в нашем списке минимальный
min_value_index=0
min_value = min(list_)
elist_=list(enumerate(list_))
# TODO заменить на enumerate
for el in elist_:
    if el[1] == min_value:
        min_value = el[1]
        min_value_index = el[0]

print("Минимальный элемент =", min_value, "находится по индексу", min_value_index)
