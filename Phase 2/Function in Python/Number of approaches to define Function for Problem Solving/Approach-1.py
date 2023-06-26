__Properties = '''

Approach-1
-----------
Function for defining addition of two Numbers
INPUT: Taking INPUT from Function Call (main program )
PROCESSING: Doing the Process in Function Body
RESULT/OUTPUT:Giving the result to Function Call

def addop(a,b):  # here a and b are called formal params
    print("-----------------------------")
    print("I am from Function Definition")
    c=a+b # Here c is called Local variable--Processing
    return c # Returing the Result to main program
#Main Program
#Accepting the Input from Main program
a = float(input("Enter First Value:"))
b = float(input("Enter Second Value:"))
c = addop(a,b) # Function call
print("sum({},{})={}".format(a,b,c)) '''

# Example:

# Write a python program by using Function for defining Subtraction of two Numbers.
# def subop(a, b):
#     c = a - b
#     return c
#
# # Main Program
# #Accepting the Input from Main program
# a = float(input("Enter First Value: "))
# b = float(input("Enter Second Value: "))
# c = subop(a, b)  # Function Call
# print("Sub ({} - {}) = {}".format(a, b, c))
#
# c = float(input("Enter First Value: "))
# d = float(input("Enter Second Value: "))
# e = subop(c, d)  # Function Call
# print("Sub ({} - {}) = {}".format(c, d, e))


# Write a python program by using Function for cal simple interest and the total amount to pay
# def simpint():
#     simpleint = (p * t * r)/100
#     return simpleint
# def totlamt():
#     totalam = p + simpint()
#     return totalam
#
# p = float(input("Enter Principle Amount: "))
# t = float(input("Enter Time: "))
# r = float(input("Enter Rate of Interest: "))
# res = simpint()
# print("Simple Interest = {}".format(res))
#
# res1 = totlamt()
# print("Total Amount = {}".format(res1))

#                                          OR

# def simpint():
#     simpleint = (p * t * r) / 100
#     totalam = p + simpint()
#     return simpleint, totalam
# p = float(input("Enter Principle Amount: "))
# t = float(input("Enter Time: "))
# r = float(input("Enter Rate of Interest: "))
# res = simpint()
# print("Simple Interest = {}".format(simpint()))
# print("Total Amount to pay = {}".format(simpint()))


# Write a python program by using Function for cal Area and Perimeter of Circle by using function.
# def area():
#     area = 3.14 * (r**2)
#     perimtr = 2 * 3.14 * r
#     return area, perimtr
#
# r = int(input("Enter Radious for Cal Area and Perimeter of Circle: "))
# area, perimtr = area()
# print("-"*100)
# print("Area of Circle = {}".format(area))
# print("-"*100)
# print("Perimeter of Circle = {}".format(perimtr))
# print("-"*100)














