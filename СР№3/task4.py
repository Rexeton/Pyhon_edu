# TODO реализовать функцию
def insert(list_,value,index=0):
    if index==0:
        list_=[value]+list_
    else:
        new_list_1=list_[:index]
        new_list_2=list_[index:]
        list_=new_list_1+[value]+new_list_2
    return list_

print(insert([1], value=0))  # [0, 1]
print(insert([0, 2], value=1, index=1))  # [0, 1, 2]
print(insert([0, 1, 2], value=3, index=3))  # [0, 1, 2, 3]
