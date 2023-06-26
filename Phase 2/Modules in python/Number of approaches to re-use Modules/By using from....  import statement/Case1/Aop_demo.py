from Aop_menu import Menu
from Aop_Operation import *
while (True):
    Menu()
    ch = int(input("Enter Your Choice: "))
    match(ch):
        case 1:
            Addop()
        case 2:
            Subop()
        case 3:
            Mulop()
        case 4:
            Divop()
        case 5:
            Mdivop()
        case 6:
            Expoop()
        case 7:
            print("Thanks for Using This Program`-`")
            break
        case _:
            print("Ur Selection of Operation is wrong-try again")

