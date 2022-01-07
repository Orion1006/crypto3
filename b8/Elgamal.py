from random import randint
from dataclasses import dataclass
from typing import List

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
        raise ValueError(f"{n} no multiplicative inverse " "mod {p}")
    else:
        return x % p



@dataclass
class OpenKey:
    p: int
    g: int
    y: int


@dataclass
class PrivKey:
    x: int


def gen_x(p):

    return randint(2, p - 1)


def gen_y(g, x, p):

    return (g ** x) % p


def gen_keys(p, g, x=None):

    x = gen_x(p) if not x else x
    y = gen_y(g, x, p)

    return OpenKey(p, g, y), PrivKey(x)


class Elgamal:
    def __init__(self, p: int, g: int, x: int = None):
        self.open_key, self.priv_key = gen_keys(p, g, x)

    def __init__(self, open_key, priv_key):
        self.open_key, self.priv_key = open_key, priv_key

    def enc(self, msg: str, k=None):

        p, g, y = self.open_key.p, self.open_key.g, self.open_key.y

        msg = to_indexes(clear_text(msg))
        enc_m = []

        for num in msg:
            k = randint(2, p - 2) if not k else k
            a = (g ** k) % p
            b = ((y ** k) * num) % p

            enc_m.append(a)
            enc_m.append(b)
        return enc_m

    def dec(self, e_msg: List[int]):
        x, p = self.priv_key.x, self.open_key.p
        d_msg = []

        for i in range(0, len(e_msg), 2):

            a, b = e_msg[i], e_msg[i + 1]
            d_msg.append(((inverse_of(a ** x, p) * b)) % p)

        return to_symbols(d_msg)




crypter = Elgamal(OpenKey(51, 2, 2), PrivKey(33))



def main():
    while True:
        print("1. Зашифровать")
        print("2. Расшифровать")
        print("0. Выйти из программы")
        cmd = input("Выберите пункт: ")
        
        if cmd == "1":
            encrypt = crypter.enc(input("Write a message: "))
            print(encrypt)
        elif cmd == "2":
            print(crypter.dec(encrypt))
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")
if __name__ == "__main__":
    main()