def gen(n, a, priv_key_A, priv_key_B):
    assert 1 < a < n
    assert all(2 < i < (n - 1) for i in (priv_key_A, priv_key_B))  # private keys

    pub_A, pub_B = (
        (a ** key) % n for key in (priv_key_A, priv_key_B)
    )  # public keys (yA, yB)

    key_A, key_B = (
        ((public ** private) % n)
        for public, private in zip((pub_A, pub_B), (priv_key_B, priv_key_A))
    )  # joint private key

    result_key = key_A if key_A == key_B and key_A > 1 else None

    return result_key


def main():
    n, a, key_A, key_B = 6, 2, 4, 3
    print("n, a, key_A, key_B", (n, a, key_A, key_B))

    res = gen(n, a, key_A, key_B)
    print("Key", res)


if __name__ == "__main__":
    main()