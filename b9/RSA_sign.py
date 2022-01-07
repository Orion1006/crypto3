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

def extended_euclidean_algorithm(a: int, b: int):
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
    assert (
        n * x + p * y
    ) % p == gcd

    if gcd != 1:
        # Или n равно 0, или p не является простым.
        raise ValueError(f"{n} no multiplicative inverse " "mod {p}")
    else:
        return x % p


def co_prime(a: int, b: int) -> bool:
  #проверка на взаимною простоту

    from math import gcd

    return gcd(a, b) == 1
    

def generate_ecp(msg, p, q, e):

    assert all(isprime(i) for i in (p, q))

    n = p * q
    assert 1 < len(msg) < n

    h = hash(msg)
    print("Hash", h)

    euler = (p - 1) * (q - 1)  # Функция Эйлера
    assert co_prime(e, euler)

    d = inverse_of(e, euler)

    return (h ** d) % n


def check(msg, ecp, e, n):
    h_1 = hash(msg)
    h = (ecp ** e) % n

    return h == h_1


def main():
    Text = input("Введите текст: ")

    p, q, e = 11, 13, 7

    msg = clear_text(Text)
    ecp = generate_ecp(msg, p, q, e)
    chk = check(msg, ecp,e , p*q)

    print("Подпись для текста", ecp)
    print("Проверяем подпись", chk)

if __name__ == "__main__":
    main()