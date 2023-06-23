__Properties = '''
Approach-4
------------
Function for defining addition of two Numbers
INPUT: Taking INPUT in Function Body
PROCESSING: Doing the Process in Function Body
RESULT/OUTPUT: Giving the result to Function Call

def addop():
    # Taking INPUT in Function Body
    k = float(input("Enter First Value:"))
    v = float(input("Enter Second Value:"))
    # Doing the Process in Function Body
    r = k + v
    #Give the result back to function call
    return k,v,r # here return can  return Multiple Values

#main program
x,y,res=addop() # Function call with Multi Line assigment
print("sum({},{})={}".format(x,y,res))
print("==============OR===============")
res = addop() # Function call with single line assigment
#Here res is an object of type tuple
print("sum({},{})={}".format(res[0],res[1],res[2]))
print("sum({},{})={}".format(res[-3],res[-2],res[-1])) '''

# Example:

# Write a python program by using Function for defining Subtraction of two Numbers.
def subop():
    # Taking INPUT in Function Body
    k = float(input("Enter First Value: "))
    v = float(input("Enter Second Value: "))
    # Doing the Process in Function Body
    r = k - v
    # Give the result back to function call
    return k, v, r  # here return can  return Multiple Values

# Main Program
p, q, res = subop()  # Function call with Multi Line assigment
print("Sub({} - {}) = {}".format(p, q, res))
print("-------------------------------------------------------------")
subtrac = subop()  # Another Function call with Single line Assignment
print("Sub({} - {}) = {}".format(subtrac[0], subtrac[1], subtrac[2]))
print("Sub({} - {}) = {}".format(subtrac[-3], subtrac[-2], subtrac[-1]))


# Write a python program by using Function for cal simple interest and the total amount to pay.
def simpint():
    p = float(input("Enter Principle Value: "))
    t = float(input("Enter Time: "))
    r = float(input("Enter Rate of Interest: "))
    si = (p*t*r)/100
    totlam = p + si
    return p, t, r, si, totlam

p, t, r, si, totlam = simpint()
print("----------------------------------------")
print("Simple Interest = {}".format(si))
print("----------------------------------------")
print("Total Amount to pay = {}".format(totlam))


# Write a python program by using Function for cal Area and Perimeter of Circle by using function.
def area():
    r = int(input("Enter Radius of Cicle for Cal Area and Perimeter: "))
    area = 3.14 * (r**2)
    perimtr = 2 * 3.14 * r

    return r, area, perimtr
r, area, perimtr = area()
print("Area of Circle = {}".format(area))
print("Perimetr of Circle = {}".format(perimtr))


# Write a python program by using Function for cal Area and Perimeter of Rectangle by using function.
def rarea():
    len = int(input("Enter Length: "))
    bred = int(input("Enter Breadth: "))
    area = len * bred
    perimtr = 2 * (len + bred)
    return len, bred, area, perimtr
# Main Program
res = rarea()
print("Area of Rectangle = {}".format(res[2]))
print("Perimeter of Rectangle = {}".format(res[3]))


# Write a python program by using Function for cal Area and Perimeter of Square,Circle by using function.
def sarea():
    s = int(input('Enter Side of given Square,Circle for Cal Area and Perimeter: '))
    area = s * s
    perimtr = 4 * s
    return s, area, perimtr

# Main Program
res = sarea()
print("Area of Square,Circle = {}".format(res[1]))
print("Perimeter of Square,Circle = {}".format(res[2]))



# Write a python program which will decide weather the given value is PALINDROME or NOT by using function.
def palindrome():
    word = input("Enter a Word/Value which is Palindrome or not: ").upper()
    pl = "PALINDROME" if word == word[::-1] else "Not PALINDROME"
    return word, pl
# Main Program
res = palindrome()
print("{} is {}".format(res[0], res[1]))



# Write a python program which will Generate a Multiplication Table by using function.
def multabls():
    num = int(input("Enter a Number You Want to Generate Multiplication Table: "))
    for i in range(1, 11):
        return num, i

# Main Program
num, i = multabls()
print("Multiplication Table of {}".format(num))
print("{} x {} = {}".format(num, i, num*i))


