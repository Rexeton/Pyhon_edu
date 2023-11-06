# TODO написать функцию remove
from typing import List
def remove(data: List[int],ind: int) -> List[int]:
    if not (ind in data):
        raise ValueError
    dd=data[::-1]
    dd.remove(ind)
    return dd[::-1]




print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
