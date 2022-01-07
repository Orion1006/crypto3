from typing import Text, Union
from sympy import isprime

def hash(msg: str, p: int = 11) -> int:
    h = 0
    h_list = []
    for symbol_code in to_indexes(msg):
        symbol_code += 1
        h = ((h + symbol_code) ** 2) % p
        h_list.append(h)
    return h

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


def co_prime(a: int, b: int) -> bool:
    from math import gcd

    return gcd(a, b) == 1

class Elgaml_ECP:
    def __init__(self, P: int, G: int):
        assert isprime(P)
        assert G < P
        self.P = P
        self.G = G

    def get_public_key(self, X: int):
        P, G = self.P, self.G
        assert 1 < X <= (P - 1)
        Y = (G ** X) % P
        return Y

    def gen_ecp(self, msg: str, K: int, X: int, h=None):
        P, G = self.P, self.G
        assert 1 < K < (P - 1) and co_prime(K, (P - 1))

        msg = clear_text(msg)

        h = hash(msg) if h is None else h
        assert 1 < h < (P - 1)

        a = (G ** K) % P
        b = ((h - X * a) * inverse_of(K, P - 1)) % (P - 1)
        return (a, b)

    def check_ecp(self, msg: str, ecp: Union[int, int], public_key: int, h=None):
        P, G = self.P, self.G
        a, b = ecp
        msg = clear_text(msg)
        h = hash(msg) if h is None else h

        A1 = ((public_key ** a) * (a ** b)) % P
        A2 = (G ** h) % P

        return A1 == A2


def main():
    Text = input("Введите текст: ")
    P, G = 13, 8

    crypter = Elgaml_ECP(P, G)

    
    X = 5
    K = 7

    ecp = crypter.gen_ecp(Text, K, X)
    chk = crypter.check_ecp(Text, ecp, crypter.get_public_key(X))

    print("Подпись пословицы", ecp)
    print("Проверка подписи", chk)

if __name__ == "__main__":
    main()