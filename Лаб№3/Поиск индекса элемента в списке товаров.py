# TODO Напишите функцию для поиска индекса товара
def f1(items_list,find_item):
    ind=None
    for el in enumerate(items_list):
        if el[1]==find_item:
            ind=el[0]
            break
    return ind
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = f1(items_list,find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
