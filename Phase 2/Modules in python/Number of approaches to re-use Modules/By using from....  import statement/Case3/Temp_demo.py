from Temperature_menu import Menu
from Temp_Operation import CtoK, CtoF, KtoC, KtoF, FtoC, FtoK
while (True):
    Menu()
    ch = int(input("Enter Your Choice: "))
    match(ch):
        case 1:
            CtoK()
        case 2:
            CtoF()
        case 3:
            KtoC()
        case 4:
            KtoF()
        case 5:
            FtoC()
        case 6:
            FtoK()
        case 7:
            print("Thanks for Using this Program")
            break
        case _:
            print("Your Selection of Operation is wrong-Please try again")


