# TODO реализовать функцию
def remove_whitespace(str_with_space):
    summ_str=""

    for el in str_with_space.split("\n"):
        for ell in el.split():
            summ_str+=ell+" "
        summ_str=summ_str[:-1]
        summ_str+="\n"
    return(summ_str[:-1])


str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
