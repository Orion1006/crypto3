abc = "абвгдежзйиклмнопрстуфхцчшщъыьэюя"

def enc(text, abc=abc, ):

    result = []

    for i, sym in enumerate(text):

        if sym not in abc:
            result.append(sym)
            continue

        n = len(abc)
        index_alph = abc.index(sym)

        shift = (index_alph + i) % n#сдвиг по индексу

        result.append(abc[shift])#вставляем в результат

    return "".join(result)


def dec(text, abc=abc):

    result = []

    for i, sym in enumerate(text):

        if sym not in abc:
            result.append(sym)
            continue

        n = len(abc)
        index_abc = abc.index(sym)

        shift = (index_abc - i) % n

        result.append(abc[shift])

    return "".join(result)

def main():
    while True:
        print("1. Зашифровать")
        print("2. Расшифровать")
        print("0. Выйти из программы")
        cmd = input("Выберите пункт: ")
        
        if cmd == "1":
            print(enc(input("Введите сообщение: "))) 
        elif cmd == "2":
            print(dec(input("Введите сообщение: "))) 
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")
if __name__ == "__main__":
    main()