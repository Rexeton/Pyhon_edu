list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Поменяйте местами значения согласно условию
elist_=enumerate(list_numbers)
i_max_num=0
max_num=list_numbers[0]
for el in elist_:
    if el[1]>=max_num:
        max_num=el[1]
        i_max_num=el[0]
list_numbers[i_max_num]=list_numbers[-1]
list_numbers[-1]=max_num
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
