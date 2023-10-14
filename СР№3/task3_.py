def delete(list_, index=None):
    # TODO реализовать функцию удаления элемента из списка по индексу
    if index is None:
        index=len(list_)-1
    if index<0:
        index=len(list_)-abs(index)
    l_1=list_[:index+1]
    l_2=list_[index+1:]
    return l_1[:len(l_1)-1]+l_2

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
