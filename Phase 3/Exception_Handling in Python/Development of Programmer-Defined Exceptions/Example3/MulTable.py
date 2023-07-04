from MultableExcept import NegativeNumError, ZeroError
def Table(n):
    num = int(n) # This Statement may Implicitly raise ValueError if num contains alnums, pure str and Symbols
    if num < 0:
        raise NegativeNumError  # Hitting the Exception
    elif num == 0:
        raise ZeroError  # # Hitting the Exception
    else: # In the case num>0
        print("---------------------------------------------")
        print("Multiple Table of {}".format(num))
        print("---------------------------------------------")
        for i in range(1,11):
            print("{} x {} = {}".format(num, i, num * i))
        print("---------------------------------------------")