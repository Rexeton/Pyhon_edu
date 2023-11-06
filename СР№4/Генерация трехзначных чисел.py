# TODO написать функцию, которая выдает трехзначное число
from random import randint
import string
def tri_topora()->str:
    num_1 = str(randint(1,9))
    num_2 = str(randint(0,9))
    num_3 = str(randint(0,9))
    return num_1+num_2+num_3

print(tri_topora())