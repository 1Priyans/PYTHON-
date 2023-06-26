# Break Statement:
__Properties = '''break is a key word

The purpose of break statement is that "To terminate the execution of loop logically when certain condition is satisfied  and PVM control 
comes of corresponding loop and executes other statements in the program".

when break statement takes place inside for loop or while loop then PVM will not execute corresponding else block(bcoz loop is not becming False) 
but it executes other statements in the program

Syntax1:
-------------------
for varname  in Iterable_object:
    ------------------------------
    if (test cond):
       break
------------------------------
Other Statement in Program 
------------------------------

Syntax2:

while(Test Cond-1):
------------------------------
    if (test cond-2):
        break
------------------------------
Other Statement in Program				
------------------------------'''

# Example:

# Program for Demonstarting break statement
# display MAV without using slicing Operation
s = "MAVERICK"
for i in s:
    if i == "E":
        break
    else:
        print("{}".format(i), end='')
else:
    print("-----------------------------")


# Disply "MAV" without using slicing                                                           OR
s = "MAVERICK"
i = 0
while i < len(s):
    if s[i] == "E":
        break

    else:
        print("{}".format(s[i]), end='')
        i = i + 1
else:
    print("-----------------------------")


# Write a Python Program which will accept any number and decide weather it is Prime Number or Not.
n = int(input("Enter the number which is prime or not: "))
if n <= 0:
    print("{} is Invalid Input".format(n))
else:
    res = "Prime"
    for i in range(2, n):  # Means 2 to (n - 1)
        if n % i == 0:
            res = "Not Prime"
            break
    if res == "Prime":
        print("{} is Prime number".format(n))

    else:
        print("{} is  not prime number".format(n))

#                                                OR

n = int(input("Enter a Number:")) # n=5
if(n <= 1):
    print("{} is invalid Input".format(n))
else:
    res = True
    for i in range(2,n):
        if(n % i == 0):
            res = False
            break
    if (res):
        print("{} Is Prime".format(n))
    else:
        print("{} is Not Prime".format(n))

#                                               OR

n = int(input("Enter a Number:")) # n=5
if(n <= 1):
    print("{} is invalid Input".format(n))
else:
    res = "HYD"
    for i in range(2, n):
        if(n % i == 0):
            res="BANG"
            break
    if(res == "HYD"):
        print("{} Is Prime".format(n))
    else:
        print("{} is Not Prime".format(n))