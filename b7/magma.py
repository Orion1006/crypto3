from pygost.gost3412 import GOST3412Magma
from pygost.utils import hexdec, hexenc
from pygost.gost3413 import ecb_encrypt, ecb_decrypt, pad2, unpad2

def encrypt(text: str, key: str) -> str:
    text, key = hexdec(text), hexdec(key)
    crypter = GOST3412Magma(key)
    return hexenc(crypter.encrypt(text))


def decrypt(text: str, key: str) -> str:
    text, key = hexdec(text), hexdec(key)
    crypter = GOST3412Magma(key)
    return hexenc(crypter.decrypt(text))


def encrypt_ecb(text: str, key: str) -> str:
    text, key = bytes(text, "utf-8"), hexdec(key)
    crypter = GOST3412Magma(key)

    res = ecb_encrypt(crypter.encrypt, crypter.blocksize, pad2(text, crypter.blocksize))

    return hexenc(res)


def decrypt_ecb(text: str, key: str) -> str:
    text, key = hexdec(text), hexdec(key)
    crypter = GOST3412Magma(key)

    res = ecb_decrypt(crypter.decrypt, crypter.blocksize, text)

    try:
        return unpad2(res, crypter.blocksize).decode()
    except ValueError:
        return res.decode()




def main():

    m = "fedcba9876543210"
    key = "ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"

    
    enc = encrypt(m, key)
    dec = decrypt(enc, key)
    print(enc,dec)

    m="Леопард не может изменить своих пятен."
    enc = encrypt_ecb(m, key)
    dec = decrypt_ecb(enc, key)
    print(enc,dec)

if __name__ == "__main__":
    main()
