def atbash(s):
    abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    return s.translate(str.maketrans(
        abc + abc.upper(), abc[::-1] + abc.upper()[::-1]))

def main():
    while True:
        print("1. Зашифровать")
        print("2. Расшифровать")
        print("0. Выйти из программы")
        cmd = input("Выберите пункт: ")
        
        if cmd == "1":
            print(atbash(input("Введите сообщение: "))) 
        elif cmd == "2":
            print(atbash(input("Введите сообщение: "))) 
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")
if __name__ == "__main__":
    main()