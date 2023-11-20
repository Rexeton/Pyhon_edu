VIKTORY_VAR = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [7, 5, 3]
]
PERVOE_POLE  = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def print_pole(pole):
    i = 1
    row = "|"
    for el in pole:
        if i % 3 != 0:
            row = row + str(pole.get(el)) + "|"
        else:
            row = row + str(pole.get(el)) + "|"
            print(row + "\n" + 7 * "-")
            row = "|"
        i += 1


def proverka(pole):
    for el in VIKTORY_VAR:
        s_x = 0
        s_o = 0
        for eel in el:
            if pole.get(str(eel)) == 'X':
                s_x += 1
            if pole.get(str(eel)) == 'O':
                s_o += 1
        if max(s_x, s_o) == 3:
            break
    return max(s_x, s_o) == 3


def proverka_hoda(pole, hod):
    return not pole.get(hod) in ('X', 'O')


def count_var(pole, viktory_var_shuf):
    mass_var = []
    for el in viktory_var_shuf:
        s_x = 0
        s_o = 0
        n_nez = []
        for eel in el:
            if pole.get(str(eel)) == 'X':
                s_x += 1
            elif pole.get(str(eel)) == 'O':
                s_o += 1
            else:
                n_nez.append(str(eel))
        mass_var.append({"CX": s_x, "CO": s_o, "незан": n_nez})
    return mass_var


def h_m(pole):
    varianti = []
    if proverka_hoda(pole, '5'):
        return '5'
    viktory_var_shuf = VIKTORY_VAR
    mass_var = count_var(pole, viktory_var_shuf)
    Toc_hod=[0,0]
    for el in mass_var:
        if (el["CO"] == 2) and len(el["незан"]) > 0:
            Toc_hod[0]=str(el["незан"][0])
        elif (el["CX"] == 2) and len(el["незан"]) > 0:
            Toc_hod[1]=str(el["незан"][0])
        if (el["CX"] == 1 and el["CO"] == 0) or (el["CX"] == 0 and el["CO"] == 1):
            for elt in el["незан"]:
                varianti.append(elt)
    if Toc_hod[0]!=0:
        return Toc_hod[0]
    if Toc_hod[1]!=0:
        return Toc_hod[1]
    return str(max(set(varianti)))


if __name__ == '__main__':
    pole = PERVOE_POLE
    print('Давай сыграем')
    print_pole(pole)
    while True:

        hod = str(input("Ваш ход "))
        while True:
            if not hod in ("1","2","3","4","5","6","7","8","9"):
                hod = str(input("Выбирите цифру на поле "))
            elif proverka_hoda(pole, hod):
                pole[hod] = 'X'
                break
            else:
                hod = str(input("Выбирите другую ячейку, эта уже занята "))
        print_pole(pole)
        if proverka(pole):
            print("Победил пользователь")
            break
        pole[h_m(pole)] = 'O'
        print("Ход терминатора")
        print_pole(pole)
        if proverka(pole):
            print("Победил терминатор")
            break
        mass = count_var(pole, VIKTORY_VAR)
        i_ver = 0
        for el in mass:
            if el["CX"] >= 1 and el["CO"] >= 1:
                i_ver += 1
        if i_ver == 8:
            print("Ничья")
            break
