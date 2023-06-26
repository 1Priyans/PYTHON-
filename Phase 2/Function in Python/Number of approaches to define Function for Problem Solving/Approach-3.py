__Properties = '''

Approach-3
----------------------------------------------------------------------------------------------------------------------------------------
Function for defining addition of two Numbers
INPUT: Taking INPUT from Function Call (main program )
PROCESSING:Doing the Process in Function Body
RESULT/OUTPUT:Display the result / output in Function Body

def addop(a,b):
    c=a+b
    print("sum({},{})={}".format(a,b,c))
#main program
x=float(input("Enter First Value:"))
y=float(input("Enter Second Value:"))
addop(x,y) # Function call'''

# Example:

# Write a python program by using Function for defining Subtraction of two Numbers.
# def subop(c, d):
#     sub = c - d
#     print("({} - {}) = {}".format(c, d, sub))
#
# # main program
# a = float(input("Enter First Value: "))
# b = float(input("Enter Second Value: "))
# subop(a, b)  # Function call


# Write a python program by using Function for cal simple interest and the total amount to pay.
# def simint():
#     si = (p * t * r) / 100
#     totlam = p + si
#     print("Simple Interest = {}".format(si))
#     print("Total Amount to pay = {}".format(totlam))
#
# p = float(input("Enter Principle Amount: "))
# t = float(input("Enter Time: "))
# r = float(input("Enter Rate of Interest: "))
#
# simint()


# Write a python program by using Function for cal Area and Perimeter of Circle by using function.
# def area(r):
#     area = 3.14 * (r**2)
#     perimtr = 2 * 3.14 * r
#     print("Area of Circle = {}".format(area))
#     print("Perimeter of Circle = {}".format(perimtr))
#
#
# # Main Program
# r = int(input("Enter Radius of Circle for Cal Area and Perimeter of Circle: "))
# area(r)


# Write a python program which will Generate a Multiplication Table by using function.
def multable():
    print("Mul Table of {}".format(num))
    for i in range(1, 11):
        print("{} x {} = {}".format(num, i, num * i))

num = int(input("Enter the Number for which you want to Generate Multiplication Table : "))
multable()


