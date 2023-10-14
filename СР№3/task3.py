# TODO реализовать функцию count
def count(list_items,value):
    i_count=0
    for el in list_items:
        if el==value:
            i_count+=1
    return i_count
list_items = [1, 2, "3", 1]
print(count(list_items, 1) == list_items.count(1))  # True
print(count(list_items, 3) == list_items.count(3))  # True
