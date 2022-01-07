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

def replace_special(text, abc=abc, replaces=REPLACES):

    for key, value in replaces.items():
        text = text.replace(key, value)
    return text


def reverse_rows(matrix):
    for i in range(1, matrix.shape[0], 2):
        matrix[i] = np.flip(matrix[i])
    return matrix


def get_text_matrix(text, cols):
    fill = cols - (len(text) % cols) if (len(text) % cols) != 0 else 0
    text = list(text) + ([" "] * fill)
    matrix = np.array(text).reshape(-1, cols)

    return reverse_rows(matrix)


def get_key(key, abc):

    key = to_indexes(key, abc)
    key = [sorted(key).index(i) for i in key]

    return key


def enc(text, key, abc=abc):
    
    cols = len(key)
    text = clear_text(text, abc)
    text_matrix = get_text_matrix(text, cols)

    key = get_key(key, abc)

    result = ["".join(text_matrix[:, i]) for i in key]
    return "".join(result)


def dec(text, key,  abc=abc):
    abc += " "
    text = clear_text(text, abc)
    cols = len(key)
    rows = len(text) // cols
    text_matrix = get_text_matrix(text, rows).transpose()

    key = get_key(key, abc)

    result = np.empty(text_matrix.shape, dtype=str)

    for i, key_i in enumerate(key):
        result[:, key_i] = (
            text_matrix[:, i] if i % 2 == 0 else np.flip(text_matrix[:, i])
        )
    result = reverse_rows(result)
    result = ["".join(item) for item in result]
    return "".join(result).strip()



def main():
    key = input("Введите ключ: ")
    while True:
        print("1. Зашифровать")
        print("2. Расшифровать")
        print("0. Выйти из программы")
        cmd = input("Выберите пункт: ")
        
        if cmd == "1":
            print(enc(input("Введите сообщение: "),key=key)) 
        elif cmd == "2":
            print(dec(input("Введите сообщение: "),key=key)) 
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")
if __name__ == "__main__":
    main()