# for loop or for....else loop:
___Properties = '''

Syntax1:-
			
for varname  in  Iterable_object:
	----------------------------------------
	    Indentation block of stmts
	----------------------------------------
---------------------------------------------------
Other statements in Program
---------------------------------------------------

Syntax2:

for   varname   in  Iterable_object:
	----------------------------------------
	Indentation block of stmts
	----------------------------------------
	else:
		----------------------------------------
		else block of statements
		----------------------------------------
---------------------------------------------------
Other statements in Program
---------------------------------------------------

Explanation:
------------
Here 'for' , "in" and 'else' are keywords

Here Iterable_object can be Sequence(bytes,bytearray,range,str), list(list,tuple),set(set,frozenset) and dict.

The execution process of for loop is that " Each of Element of Iterable_object selected , placed in varname and executes Indentation block of 
statements".This Process will be repeated until all elements of Iterable_object completed.

when all the elements of Iterable Object completed  then PVM  comes out of for loop and executes else block of statements which are written 
under else block 

Writing else block is optional.'''

# Example:

# Program for Implementing string data
s = "MAVERICK"
for i in s:
    print("\t{}".format(i))
print("---------------------------")

# for Reverse order
s = "MAVERICK"
for i in s[::-1]:
    print("\t{}".format(i))
print("---------------------------")

# Write a Python Program which will display one to n numbers using for loop.
n = int(input("Enter how many Numbers you want to Generate: "))
if n <= 1:
    print("{} is Invalid Inpput".format(n))

else:
    print("------------------------------------")
    print("Natural Numbers within {} is".format(n))
    for i in range(1, n + 1):
        print("\t{}".format(i))
    else:
        print("________________________________")


# Write a Python Program which will display n to one numbers using for loop.
n = int(input("Enter how many Numbers you want to Generate: "))
if n <= 1:
    print("{} is Invalid Inpput".format(n))

else:
    print("------------------------------------")
    print("Natural Numbers within {} is".format(n))
    for i in range(n, 0, -1):
        print("\t{}".format(i))
    else:
        print("________________________________")


# Write a Python Program which will generate Odd numbers within n numbers by using for loop.
n = int(input("Enter how many Numbers you want to Generate: "))
if n <= 1:
    print("{} is Invalid Inpput".format(n))

else:
    print("------------------------------------")
    print("Odd Numbers within {} is".format(n))
    for i in range(1, n + 1, 2):
        print("\t{}".format(i))
    else:
        print("________________________________")



# Write a Python Program which will generate Even numbers within n numbers by using for loop.
n = int(input("Enter how many Numbers you want to Generate: "))
if n <= 1:
    print("{} is Invalid Inpput".format(n))

else:
    print("------------------------------------")
    print("Odd Numbers within {} is".format(n))
    for i in range(2, n + 1, 2):
        print("\t{}".format(i))
    else:
        print("________________________________")


# Write a Python Program which will find Sum of first n natural numbers, Squares of n natural numbers and Cubes of n natural numbers.
n = int(input("Enter How many numbers Do you want to Generate: "))
if n <= 0:
    print("{} is Invalid Input".format(n))

else:
    print("________________________________________________________________________________________________________________")
    print("Natural Nums {}  Square Nums {}  Cubes Nums {}".format(n,n,n))
    s, ss, c = 0, 0, 0
    for i in range(1, n + 1):
        print("\t\t\t{}  \t\t\t{}  \t\t\t{} ".format(i, i, i))
        s, ss, c = s + i, ss + i ** 2, c + i ** 3
    else:
        print("________________________________________________________________________________________________________________")
        print("\t\t\t{} \t\t\t{} \t\t\t{}".format(s, ss, c))
        print("________________________________________________________________________________________________________________")

# Write a python program which will cal Factorial of a given number.
n = int(input("Enter Number for cal Factorial: "))
if n < 0:
    print("{} is Invalid Input".format(n))

else:
    print("----------------------------------------------------")
    print("Factorial numbers within {}".format(n))
    print("----------------------------------------------------")
    f = 1
    for i in range(1, n + 1):
        f = f * i

    else:
        print("Factorial({}!) = {}".format(n, f))


# Write a python program which will generate Multiplication Table for the given positive integer value.
n = int(input("Enter the Number for which you want to Generate Multiplication Table : "))
if n <= 1:
    print("{} is Invalid input".format(n))

else:
    print("----------------------------------------")
    print("Multiplication Table of {}".format(n))
    print("----------------------------------------")
    for i in range(1, 11):
        print("\t\t{} × {} = {}".format(n, i, n * i))
    else:
        print("----------------------------------------")



