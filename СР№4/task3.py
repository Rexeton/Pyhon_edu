import random as r


def get_unique_list_numbers() -> list[int]:
    # data = []
    # while len(data) != 15:
    #     rand_num = r.randrange(-10, 10 + 1)
    #     if not rand_num in data:
    #         data.append(rand_num)
    # return data
    return r.sample([el for el in range(-10,10+1)],k=15)

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
