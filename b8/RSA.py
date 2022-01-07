from typing import List
import numpy as np

abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

REPLACES = {
    ",": "ЗПТ",
    ".": "ТЧК",
    "-": "ТИРЕ",
    ";": "ТЧКИЗПТ",
}

def clear_text(text, abc=abc):
    import re

    text = replace_special(text, abc)
    text = text.lower()
    text = re.sub(f"[^{abc}]", "", text)
    return "".join([symbol for symbol in text.lower() if symbol in abc])

def to_indexes(text, abc=abc):
    return [abc.index(symbol) for symbol in text]

def to_symbols(nums, abc=abc):
    return "".join([abc[num] for num in nums])

def replace_special(text, abc=abc, replaces=REPLACES):

    for key, value in replaces.items():
        text = text.replace(key, value)
    return text


def extended_euclidean_algorithm(a: int, b: int) :
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

def inverse_of(n: int, p: int) -> int:
   
    gcd, x, y = extended_euclidean_algorithm(n, p)
    assert (n * x + p * y) % p == gcd

    if gcd != 1:
        raise ValueError(f"{n} нет инверсии {p}")
    else:
        return x % p


class RSA:
    def __init__(self, open_key: List[int], private_key: List[int]):
        assert open_key[1] == private_key[1]
        self.open_key = open_key
        self.private_key = private_key

    @classmethod
    def init_params(cls, p: int, q: int, e: int):
        n = p * q
        euler = (p - 1) * (q - 1)  # Функция Эйлера

        d = inverse_of(e, euler)  # Cекретная экспонента

        return cls((e, n), (d, n))

    @property  # Открытый ключ
    def open_key(self):
        return self.e, self.n

    @open_key.setter
    def open_key(self, key):
        self.n = key[1]
        self.e = key[0]

    @property  # Закрытый ключ
    def private_key(self):
        return self.d, self.n

    @private_key.setter
    def private_key(self, key):
        self.n = key[1]
        self.d = key[0]

    def enc_1(self, num: int):
        return (num ** self.e) % self.n

    # Шифрование
    def enc(self, m: str):
        m = to_indexes(clear_text(m))
        enc_m = [self.enc_1(symbol) for symbol in m]
        return enc_m

    def dec_1(self, num: int):
        return (num ** self.d) % self.n

    # Расширвание
    def dec(self, enc_m: List[int]):
        m = [self.dec_1(symbol) for symbol in enc_m]
        m = to_symbols(m)
        return m


encrypter = RSA((77, 2849), (533, 2849))

def main():
    while True:
        print("1. Зашифровать")
        print("2. Расшифровать")
        print("0. Выйти из программы")
        cmd = input("Выберите пункт: ")
        
        if cmd == "1":
            encrypt = encrypter.enc(input("Write a message: "))
            print(encrypt)
        elif cmd == "2":
            print(encrypter.dec(encrypt))
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")
if __name__ == "__main__":
    main()