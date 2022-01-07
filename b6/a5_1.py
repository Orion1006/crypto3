import re
import copy
import sys 
from typing import List
reg_x_length = 19
reg_y_length = 22
reg_z_length = 23

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


def replace_special(text, abc=abc, replaces=REPLACES):

    for key, value in replaces.items():
        text = text.replace(key, value)
    return text

def to_binary(plain: str) -> List[int]:
    """Converts plaintext to binary"""

    binary = [
        int(i)
        for i in "".join(block[2:] for block in map(bin, bytearray(plain, "utf-8")))
    ]

    return binary


def bin_to_str(
    bits: str, encoding: str = "UTF-8", errors: str = "surrogatepass"
) -> str:
    """Converts binary to string."""

    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode(encoding, errors) or "\0"


key_one = ""
reg_x = []
reg_y = []
reg_z = []

def loading_registers(key): #loads registers using a 64-bit key as a parameter
    i = 0
    while(i < reg_x_length): 
        reg_x.insert(i, int(key[i])) #takes first 19 elements from key
        i = i + 1
    j = 0
    p = reg_x_length
    while(j < reg_y_length): 
        reg_y.insert(j,int(key[p])) #takes next 22 elements from key
        p = p + 1
        j = j + 1
    k = reg_y_length + reg_x_length
    r = 0
    while(r < reg_z_length): 
        reg_z.insert(r,int(key[k])) #takes next 23 elements from key
        k = k + 1
        r = r + 1

def set_key(key): #sets the key and loads the registers if it contains 0's and 1's and if it's exactly 64 bits 
    if(len(key) == 64 and re.match("^([01])+", key)):
        key_one=key
        loading_registers(key)
        return True
    return False

def get_key(): #gets the keyfrom typing import List
    return key_one




def get_majority(x,y,z): #gets majority by adding up the x,y,and z values and if it's greater than 1 (e.g. two 1's and one 0), it returns the majority (1). Otherwise, if it's two 0's and one 1, the majority is returned as 0.
    if(x + y + z > 1):
        return 1
    else:
        return 0

def get_keystream(length): #calculates the keystream by XOR-ing the appropriate indeces
    reg_x_temp = copy.deepcopy(reg_x)
    reg_y_temp = copy.deepcopy(reg_y)
    reg_z_temp = copy.deepcopy(reg_z)
    keystream = []
    i = 0
    while i < length:
        majority = get_majority(reg_x_temp[8], reg_y_temp[10], reg_z_temp[10])
        if reg_x_temp[8] == majority: 
            new = reg_x_temp[13] ^ reg_x_temp[16] ^ reg_x_temp[17] ^ reg_x_temp[18]
            reg_x_temp_two = copy.deepcopy(reg_x_temp)
            j = 1
            while(j < len(reg_x_temp)):
                reg_x_temp[j] = reg_x_temp_two[j-1]
                j = j + 1
            reg_x_temp[0] = new

        if reg_y_temp[10] == majority:
            new_one = reg_y_temp[20] ^ reg_y_temp[21]
            reg_y_temp_two = copy.deepcopy(reg_y_temp)
            k = 1
            while(k < len(reg_y_temp)):
                reg_y_temp[k] = reg_y_temp_two[k-1]
                k = k + 1
            reg_y_temp[0] = new_one

        if reg_z_temp[10] == majority:
            new_two = reg_z_temp[7] ^ reg_z_temp[20] ^ reg_z_temp[21] ^ reg_z_temp[22]
            reg_z_temp_two = copy.deepcopy(reg_z_temp)
            m = 1
            while(m < len(reg_z_temp)):
                reg_z_temp[m] = reg_z_temp_two[m-1]
                m = m + 1
            reg_z_temp[0] = new_two

        keystream.insert(i, reg_x_temp[18] ^ reg_y_temp[21] ^ reg_z_temp[22])
        i = i + 1
    return keystream




def encrypt(plain): #takes in a plaintext, converts it to binary, gets the keystream after inputting the length of the binary, and appends the XOR values of the keystream and binary to a string
    s = ""
    binary = to_binary(clear_text(plain))
    keystream = get_keystream(len(binary))
    i = 0
    while(i < len(binary)):
        s = s + str(binary[i] ^ keystream[i])
        i = i + 1
    return s

def decrypt(cipher): #takes in a cipher, gets the keystream from its length, cipher is XOR'd with keystream, and converted to string 
    s = ""
    binary = []
    keystream = get_keystream(len(cipher))
    i = 0
    while(i < len(cipher)):
        binary.insert(i,int(cipher[i]))
        s = s + str(binary[i] ^ keystream[i])
        i = i + 1
    print(str(s))
    return bin_to_str(str(s))

def user_input_key(): #input the key from the console
    tha_key = str(input('Введите 64-битный ключ: '))
    if (len(tha_key) == 64 and re.match("^([01])+", tha_key)):
        return tha_key
    else:
        while(len(tha_key) != 64 and not re.match("^([01])+", tha_key)):
            if (len(tha_key) == 64 and re.match("^([01])+", tha_key)):
                return tha_key
            tha_key = str(input('Введите 64-битный ключ: '))
    return tha_key

def user_input_choice(): #input the choice from the console
    someIn = str(input('[0]: Выход\n[1]: Зашифровать\n[2]: Расшифровать\n: '))
    if (someIn == '0' or someIn == '1' or someIn == '2'):
        return someIn
    else:
        while(someIn != '0' or someIn != '1' or someIn != '2'):
            if (someIn == '0' or someIn == '1' or someIn == '2'):
                return someIn
            someIn = str(input('[0]: Выход\n[1]: Зашифровать\n[2]: Расшифровать\n:  '))
    return someIn

def user_input_plaintext(): #input plaintext in console
    try:
        someIn = str(input('Введите текст: '))
    except:
        someIn = str(input('Попробуйте еще раз: '))
    return someIn

def user_input_ciphertext(): #input ciphertext in console
    ciphertext = str(input('Введите гипертекст: '))
    if (re.match("^([01])+", ciphertext)):
        return ciphertext
    else:
        while(not re.match("^([01])+", ciphertext)):
            if (re.match("^([01])+", ciphertext)):
                return ciphertext
            ciphertext = str(input('Попробуйте еще раз: '))
    return ciphertext

def main(): #the main function that processes user inputs 
    key = str(user_input_key())
    set_key(key)
    first_choice = user_input_choice()
    if(first_choice == '0'):
        sys.exit(0)
    elif(first_choice == '1'):
        plaintext = str(user_input_plaintext())
        print(plaintext)
        a = encrypt(plaintext)
        b = decrypt(a)
        print(a,b)
    elif(first_choice == '2'):
        ciphertext = str(user_input_ciphertext())
        print(decrypt(ciphertext))			

#Пример ключа: 0101001000011010110001110001100100101001000000110111111010110111


if __name__ == "__main__":
    main()