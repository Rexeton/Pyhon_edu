# TODO Найдите количество книг, которое можно разместить на дискете
value_all=1.44 #Mb
sheet_in_book=100
row_in_sheet=50
symbol_in_row=25
weight_of_one_symb=4 #b


weight_of_one_book=weight_of_one_symb*symbol_in_row*row_in_sheet*sheet_in_book/1024/1024


print("Количество книг, помещающихся на дискету:", int(value_all//weight_of_one_book))
