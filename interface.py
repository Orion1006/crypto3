from b1.atbash import main as atb_main
from b1.Cesar import main as ces_main
from b1.Polibiy import main as pol_main
from b2.tritemi import main as tri_main
from b2.vishiner import main as vis_main
from b2.belazo import main as b_main
from b3.matrix import main as matrix_main
from b3.plaiferpy import main as plaifer_main
from b4.kardano import main as kardano_main
from b4.perestanovka import main as perestanovka_main
from b5.shenon import main as shenon_main
from b6.a5_1 import main as a5_main
from b7.magma import main as magma_main
from b8.Elgamal import main as elgamal_main
from b8.RSA import main as rsa_main
from b9.Elgamal_sign import main as el_sign_main
from b9.RSA_sign import main as rsa_sign_main
from b10.gost_34_10_94 import main as gost_main
from b11.Helman import main as helman_main



def the_main():
    while True:
        print("1. Атбаш")
        print("2. Цезарь")
        print("3. Полибий")
        print("4. Белазо")
        print("5. Тритемий")
        print("6. Вижинер")
        print("7. Матричный")
        print("8. Плейфер")
        print("9. Кардано")
        print("10. Перестановка")
        print("11. Шенон")
        print("12. А5_1")
        print("13. Магма")
        print("14. Эльгамаль")
        print("15. RSA")
        print("16. Эльгамаль подпись")
        print("17. RSA подпись")
        print("18. Гост 34_10")
        print("19. Хеллман")
        print("0. Выйти из программы")
        cmd = input("Выберите пункт: ")
        
        
        if cmd == "1":
            atb_main()
        elif cmd == "2":
            ces_main()
        elif cmd == "3":
            pol_main()
        elif cmd == "4":
            b_main()
        elif cmd == "5":
            tri_main()
        elif cmd == "6":
            vis_main()
        elif cmd == "7":
            matrix_main()
        elif cmd == "8":
            plaifer_main()
        elif cmd == "9":
            kardano_main()
        elif cmd == "10":
            perestanovka_main()
        elif cmd == "11":
            shenon_main()
        elif cmd == "12":
            a5_main()
        elif cmd == "13":
            magma_main()
        elif cmd == "14":
            elgamal_main()
        elif cmd == "15":
            rsa_main()
        elif cmd == "16":
            el_sign_main()
        elif cmd == "17":
            rsa_sign_main()
        elif cmd == "18":
            gost_main()
        elif cmd == "19": 
            helman_main()           
        elif cmd == "0":
            break
        else:
            print("Вы ввели не правильное значение")
if __name__ == "__main__":
    the_main()		

