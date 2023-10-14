# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group,participants_second_group,flesh=","):
    spisok_1=set(participants_first_group.split(flesh))
    spisok_2 = set(participants_second_group.split(flesh))
    itog=list(spisok_1.intersection(spisok_2))
    itog.sort()
    return itog
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group,"|"))