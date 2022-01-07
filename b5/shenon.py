abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

M = 33
A = 4
C = 9
T0 = 17

REPLACES = {
    ",": "ЗПТ",
    ".": "ТЧК",
    "-": "ТИРЕ",
    ";": "ТЧКИЗПТ",
}


def to_indexes(text, abc=abc):
    return [abc.index(symbol) for symbol in text]


def to_symbols(nums, abc=abc):
    return "".join([abc[num] for num in nums])


def clear_text(text, abc=abc):
    import re

    text = replace_special(text, abc)
    text = text.lower()
    text = re.sub(f"[^{abc}]", "", text)
    return "".join([symbol for symbol in text.lower() if symbol in abc])


def replace_special(text, abc=abc, replaces=REPLACES):

    for key, value in replaces.items():
        text = text.replace(key, value)
    return text

def lcg(m, a, c, seed, _range):
    for _ in range(_range):
        seed = (a * seed + c) % m
        yield seed

def enc(text: str, alph: str = abc, **kwargs) -> str:
    gamma = [*lcg(M, A, C, T0, len(text))]
    result = [
        (i + j + 1) % M
        for i, j in zip(
            to_indexes(clear_text(text, alph), alph),
            gamma,
        )
    ]

    return " ".join(map(str, result))


def dec(text: str, alph: str = abc, **kwargs):
    text = list(map(int, text.split(" ")))
    gamma = [*lcg(M, A, C, T0, len(text))]
    result = [
        (i - j - 1) % M
        for i, j in zip(
            text,
            gamma,
        )
    ]
    result = to_symbols(result, alph)

    return result



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