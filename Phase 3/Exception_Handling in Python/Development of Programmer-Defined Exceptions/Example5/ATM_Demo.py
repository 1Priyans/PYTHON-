# ATM_Demo.py--------> Main Program
from ATM_Menu import Menu
from ATMOperation import Deposit, Withdraw, Balenq
from ATMExcept import DepositError, WithDrawError, InSuffFundError
while (True):
    Menu()
    try:
        ch = int(input("Enter Your Choice: "))
        match ch:
            case 1:
                try:
                    Deposit()
                except DepositError:
                    print("Don't Enter -ve/zero for Deposit Amount")
                except ValueError:
                    print("Don't try to Deposit Alphanums, str and symbols")
            case 2:
                try:
                    Withdraw()
                except WithDrawError:
                    print("Don't Enter -ve/zero for Deposit Amount")
                except InSuffFundError:
                    print("Your Account does not have Suff Funds")
                except ValueError:
                    print("Don't try to Deposit Alphanums, str and symbols")
            case 3:
                Balenq()
            case 4:
                print("Thanks for Using This Program")
                break
            case _:
                print("Your Selection of Operation is Wrong--Try again")
    except ValueError:
        print("Don't enter Alphanums, pure str and symbols from choice")
