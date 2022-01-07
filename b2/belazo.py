abc = "абвгдежзиклмнопрстуфхцчшщыьэюя"


def create_row(sym, abc):#строка для матрицы алфавита 
    row = abc[abc.index(sym) :] + abc[: abc.index(sym)]

    return row


def create_table(key, abc):#матрица для алфавита

    table = [abc]

    for sym in key:

        row = create_row(sym, abc)
        table.append(row)

    return table


def enc(text, key, abc=abc, ):

    result = []
    for i, sym in enumerate(text):

        sym = sym.lower()

        if sym not in abc:

            result.append(sym)
            continue

        key_row_index = i % len(key)
        col_index = abc.index(sym)

        row = create_row(key[key_row_index], abc)
        enc_sym = row[col_index]

        result.append(enc_sym)

    return "".join(result)


def dec(text, abc=abc, key=None,  **kwargs):
   
    result = []
    for i, sym in enumerate(text):

        sym = sym.lower()

        if sym not in abc:

            result.append(sym)
            continue

        key_row_index = i % len(key)
        row = create_row(key[key_row_index], abc)

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