import numpy as np
abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"


def to_indexes(text, abc):
    return [abc.index(symbol) for symbol in clear_text(text, abc)]


def to_symbols(nums, abc):
    return "".join([abc[num] for num in nums])


def clear_text(text, abc):
    return "".join([symbol for symbol in text if symbol in abc])


def is_int(num):
    return num % int(num) == 0


def to_slices(items, step):
    return [items[i : i + step] for i in range(0, len(items), step)]


def check_key(key):

    key_sqrt = np.sqrt(len(key))
    assert is_int(key_sqrt)
    key_sqrt = int(key_sqrt)

    return key_sqrt


def text_to_matrix(text, abc, cols):
    text_indexes = to_indexes(text, abc)
    matrix = np.asmatrix(to_slices(text_indexes, cols))

    return matrix


def nums_to_vectors(nums, cols):
    vectors = [np.array(vec) for vec in to_slices(nums, cols)]

    if len(vectors[-1]) != cols:

        last_sym = vectors[-1][-1]

        vectors[-1] = np.append(
            vectors[-1],
            np.array([last_sym] * (cols - len(vectors[-1]))),
        )

    vectors = [np.asmatrix(vec).T for vec in vectors]

    return vectors


def enc(text, key, abc=abc):

    abc += "., ?"
    text = text.lower()

    key_sqrt = check_key(key)

    text_indexes = to_indexes(text, abc)
    text_vectors = nums_to_vectors(text_indexes, key_sqrt)

    key_mat = text_to_matrix(key, abc, key_sqrt)

    result = [key_mat * vec for vec in text_vectors]
    result = [item.item() for matrix in result for item in matrix]

    return " ".join([str(item) for item in result])


def dec(nums, key, abc=abc ):

    abc += "., ?"

    if type(nums) == str:
        nums = [int(num) for num in nums.split(" ")]

    key_sqrt = check_key(key)

    inv_key_matrix = np.linalg.inv(text_to_matrix(key, abc, key_sqrt))
    vectors = nums_to_vectors(nums, key_sqrt)

    result = [inv_key_matrix * vec for vec in vectors]
    result = [int(item.item() + 0.5) for matrix in result for item in matrix]
    result = to_symbols(result, abc)

    return result

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