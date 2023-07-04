# ATMOperation.py-----> File Name and Module Name
from ATMExcept import DepositError, WithDrawError, InSuffFundError
bal = 500.00 # Here bal is called Global Variable
def Deposit():
    damt = float(input("Enter Your Deposit Amount: "))  # May implicitly raises ValueError
    if damt <= 0:
        raise DepositError
    else:
        global bal
        bal = bal + damt
        print("Your Account xxxxxxx123 Credited with INR.{}".format(damt))
        print("Now Your Account xxxxxxx123 Balance is INR.{}".format(bal))
def Withdraw():
    global bal
    wamt = float(input("Enter Your Withdraw Amount: "))  # # May implicitly raises ValueError
    if wamt <= 0:
        raise WithDrawError
    elif wamt + 500 > bal:
        raise InSuffFundError
    else:
        bal = bal - wamt
        print("Your Account xxxxxxx123 Debited with INR.{}".format(wamt))
        print("Now Your Account xxxxxxx123 Balance after withdraw INR.{}".format(bal))
def Balenq():
    print("Account xxxxxxxxx123 Balance INR.{}".format(bal))