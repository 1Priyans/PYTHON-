# Operation2.py ----> File Name and Module Name (M_runner.py is in folder python2.0 ---> M_Operation
def Div():
    print("Enter the Following Values for Division")
    a, b = float(input("Enter First Value: ")), float(input("Enter Second Value: "))

    print("Division of {}/{} = {}".format(a,b,a/b))
    print("Floor Division of {}//{} = {}".format(a,b,a//b))

def Mod_div():
    print("Enter the Following Values for Modulo Division")
    a, b = float(input("Enter First Value: ")), float(input("Enter Second Value: "))
    print("Modulo Division of {} % {} = {}".format(a,b,a % b))

def Expo():
    print("Enter the Following Values for Exponentiation")
    a, b = float(input("Enter Base: ")), float(input("Enter Power: "))
    print("Exponentiation of {} ** {} = {}".format(a, b, a ** b))