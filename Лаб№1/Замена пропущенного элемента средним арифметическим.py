numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
# i=0
# for el in numbers:
#     if el is None:
#         numbers[i] = 0
#         numbers[i] = sum(numbers)/(len(numbers))
#     i += 1

index = numbers.index(None)
numbers[index] = (sum(numbers[:index]) + sum(numbers[index + 1:])) / len(numbers)
print("Измененный список:", numbers)
