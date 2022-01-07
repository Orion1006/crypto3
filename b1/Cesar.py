abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

DEFAULT_KEY = 3
def is_int(s):
    if s[0] in ("-", "+"):
        return s[1:].isdigit()
    return s.isdigit()

def alph_shift_func(alph: str, key: int) -> str:
    return "".join([alph[(alph.index(sym) + key) % len(alph)] for sym in alph])





def enc(text: str, alph: str = abc, key: str = DEFAULT_KEY, **kwargs) -> str:
    assert is_int(key), "Введите цифровой ключ"
    key = int(key)
    alph_shift = alph_shift_func(alph, key)

    return text.translate(
        str.maketrans(alph + alph.upper(), alph_shift + alph_shift.upper())
    )


def dec(text: str, alph: str = abc, key: str = DEFAULT_KEY, **kwargs) -> str:
    assert is_int(key), "Введите цифровой ключ"
    key = int(key)
    alph_shift = alph_shift_func(alph, key)

    return text.translate(
        str.maketrans(alph_shift + alph_shift.upper(), alph + alph.upper())
    )

def main():
    while True:
        key = input("Введите ключ: ")
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

