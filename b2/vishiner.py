abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

def create_row(sym, abc):
    row = abc[abc.index(sym) :] + abc[: abc.index(sym)]

    return row

def enc(text, key, abc=abc):

    assert len(key) == 1, "Длина ключа должна быть равна 1"

    result = []
    gamma = [key]

    for sym in text:

        sym = sym.lower()
        if sym not in abc:
            continue
        col_index = abc.index(sym)

        row = create_row(gamma[-1], abc)

        enc_sym = row[col_index]

        gamma.append(enc_sym)
        result.append(enc_sym)

    return "".join(result)


def dec(text, key, abc=abc):

    result = []
    gamma = key + text

    for i, sym in enumerate(text):

        sym = sym.lower()

        if sym not in abc:
            continue

        row = create_row(gamma[i], abc)
        col_index = row.index(sym)

        enc_sym = abc[col_index]

        result.append(enc_sym)

    return "".join(result)


def main():
    key = input("Введите ключ: ")
    while True:
        print("1. Зашифровать")
        print("2. Расшифровать")
        print("0. Выйти из программы")
        cmd = input("Выберите пункт: ")
        
        if cmd == "1":
            print(enc(input("Введите сообщение: "), key=key)) 
        elif cmd == "2":
            print(dec(input("Введите сообщение: "), key=key)) 
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")
if __name__ == "__main__":
    main()