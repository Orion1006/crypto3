abc = "абвгдеёжзиклмнопрстуфхцчшщыьэюя"

def alph_to_sq(abc, cols=6):

    from math import ceil, sqrt

    n = ceil((sqrt(len(abc))))  # получение размера квадратной матрицы
    sq = [[char for char in abc[i * n : (i + 1) * n]] for i in range(n)]

    return sq


def enc(text, abc=abc):

    answer = []
    sq = alph_to_sq(abc)

    for sym in text:
        sym = sym.lower()

        for row in sq:
            if sym not in row:
                continue
            num = [sq.index(row) + 1, row.index(sym) + 1]
            answer.append(num)

    return answer


def dec(nums, abc=abc):

    sq = alph_to_sq(abc)

    return "".join([sq[sym[0] - 1][sym[1] - 1] for sym in nums])




def main():
    while True:
        print("1. Зашифровать")
        print("2. Расшифровать")
        print("0. Выйти из программы")
        cmd = input("Выберите пункт: ")
        
        if cmd == "1":
            encrypt = enc(input("Write a message: "))
            print(encrypt)
        elif cmd == "2":
            print(dec(encrypt))
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")
if __name__ == "__main__":
    main()