from Figure_menu import Menu
from Circle import Area as cr
from Rect import Area as rr
from Square import Area as sr
from Triangle import Area as tr

while(True):
    Menu()
    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        cr()
    elif ch == 2:
        rr()
    elif ch == 3:
        sr()
    elif ch == 4:
        tr()
    elif ch == 5:
        print("Thanks For Using this Program")
        break
    else:
        print("Your Selection of Operaation is Wrong Please try again")




