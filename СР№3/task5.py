# TODO реализовать функцию
def get_sentences_list(str_work):
    str_new=str_work.split(".")
    i=0
    new_list=[]
    for el in str_new:
        str_new[i]=el.strip()
        if str_new[i]!="":
            new_list+=[str_new[i]]
        i+=1

    return new_list
print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
