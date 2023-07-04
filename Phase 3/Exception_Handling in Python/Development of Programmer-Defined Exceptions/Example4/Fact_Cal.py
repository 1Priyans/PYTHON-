# Fact_Cal.py------> File Name and Module Name
from FactExcept import NegNumError
def Fact(n):
    num = int(n)  # If n is Alphanum, str and Symbols then it raises ValueError
    if num<0:
        raise NegNumError
    else:
        f = 1
        for i in range(1, num + 1):
            f = f * i
        print("Factorial({}) = {}".format(num, f))
