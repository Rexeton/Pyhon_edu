ALLOW_SYMBOLS = ["0", "1"]  # Допустимые символы


def check_string(str_):
    prov=True
    if str_=="":
        prov = False
    for el in str_:
        if not el in ALLOW_SYMBOLS:
            prov=False
            break
    return prov
print(check_string("1010101010"))
print(check_string("101021231010103"))
print(check_string("asdawqe"))
print(check_string(""))
