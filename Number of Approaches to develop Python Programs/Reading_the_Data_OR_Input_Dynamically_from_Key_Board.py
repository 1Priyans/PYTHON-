# To read the Data OR Input Dynamically from Key Board, we have 2 pre-defined Functions. They are
# 1) input()
__Properties = '''              Syntax:-  varname=input()

1) Here input() is used for Reading the any type of data in the form of str from Key Board and place that 
    value in LHS Varname.

2) Programmatically, we can convert str type data into any possible data type value by using Typecasting Techniques. '''
# Example:
#a) program for accepting a values and display it on console
print("Enter the value of a:" )
a = input()
print(a,type(a))


# 2.) input(message):
__Properties = '''              Syntax:-    varname=input(Message)

1) Here Message represents any string data and It is one of the User-Prompting Message

2)here input(Message) is used for Reading the any type of data in the form of str from Key Board and place that value in LHS 
Varname along with It also gives User-Prompting Message.

3)Programatically, we can convert str type data into any possible data type value by using Typcasting Techniques. '''
#b) program for accepting Two Numerical Values from KBD and Multiply them
a = input("Enter the First Value  ")
b = input("Enter the Second Value ")
print(a,type(a))
print(b,type(b))
# TypeError: a*b
# convert a and b(Which is str type) into float type
c = float(a)
d = float(b)
print(c,type(c))
print(d,type(d))
e = c*d
print("-"*60)
print("Value of c = {}".format(c))
print("Value of d = {}".format(d))
print("Mul {}".format(e))
print("-"*60)

#                                        "OR"

a = float(input("Enter the First Value  "))
b = float(input("Enter the Second Value "))
c = a*b
print("-"*60)
print("Value of a = {}".format(a))
print("Value of b = {}".format(b))
print("Mul {}".format(c))
print("-"*60)

#                                        "OR"

print("Enter Two Values")
a = float(input())
b = float(input())
c = a*b
print("-"*60)
print("Value of a = {}".format(a))
print("Value of b = {}".format(b))
print("Mul {}".format(c))
print("-"*60)

#                                        "OR"

c = (float(input("Enter First Value ")) * float(input("Enter Second Value ")))
print("-"*60)
print("Mul {}".format(c))
print("-"*60)

#                                        "OR"

print("Mul {}".format(float(input("Enter First Value ")) * float(input("Enter Second Value "))))

#                                        "OR"

# Program for cal area and Perimeter of Rectangle
lth = float(input("Enter the Length "))
bth = float(input("Enter the Breadth "))
ar = lth * bth
peri = 2*(lth + bth)
print("-"*60)
print("\tLength = {}".format(lth))
print("\tBreadth = {}".format(bth))
print("\tArea of Rectangle = {} ".format(ar))
print("\tPerimeter of Rectangle = {}".format(peri))
print("-"*60)

#                                        "OR"

# program for cal Area and Perimeter  of Circle
rad = float(input("Enter the Radius of Given Circle: "))
ar = 3.14 * (rad * rad)
peri = (2 * 3.14 * rad)
print("*"*60)
print("Radius of Circle %.2f" %rad)
print("Area = %.2f" %ar)
print("Perimeter = %.2f" %peri)
print("*"*60)


