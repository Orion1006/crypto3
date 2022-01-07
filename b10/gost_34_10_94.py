from typing import Union

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


def get_hash(
    message: str,
    q: int,
    h: int = None,
):
    hashed_m = h if h else hash(message)
    hashed_m = 1 if hashed_m % q == 0 else hashed_m

    return hashed_m

def primes(n):
    """
    Факторизация числа n
    """
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)  
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac



def enc(text: str, P: str, Q: str, A: str, X: str, K: str, h: int = None):
    P, Q, A, X, K = map(int, (P, Q, A, X, K))
    assert Q in primes(P - 1)
    assert (A ** Q) % P == 1
    assert 1 < A < (P - 1)
    assert X < Q
    assert K < Q

    text = clear_text(text)

    text_hash = get_hash(text, Q, h)

    r = ((A ** K) % P) % Q
    assert r != 0

    s = (X * r + K * text_hash) % Q
    return f"{r},{s}"


def dec(text: str, P: str, Q: str, A: str, Y: str, ecp: str, h: int = None):
    r, s = map(int, ecp.split(","))
    P, Q, Y, A = map(int, (P, Q, Y, A))
    text = clear_text(text)

    hashed_m = get_hash(text, Q, h)

    v = (hashed_m ** (Q - 2)) % Q
    z1 = (s * v) % Q
    z2 = ((Q - r) * v) % Q
    u = ((A ** z1 * Y ** z2) % P) % Q

    return u == r


def main():
    text = input("Введите текст: ")

    p, q, a = 23, 11, 8
    k = 7
    x = 9
    y = (a ** x) % p

    ecp = enc(text, p, q, a, x, k)
    chk = dec(text, p, q, a, y, ecp)
    print("Подпись пословицы", ecp)
    print("Проверка подписи", chk)


if __name__ == "__main__":
    main()