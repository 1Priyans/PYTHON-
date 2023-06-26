# while loop or while.....else loop:
__Properties = '''

Syntax: 

while (Test Cond):
-----> Statement 1
-----> Statement 1
-----> ___________
-----> Statement-n
---------------------------
Other Statements in Programming
____________________________
             OR
             
while (Test Cond):
-----> Statement 1
-----> Statement 1
-----> ___________
-----> Statement-n
else:
-----> else Block of statements
---------------------------
Other Statements in Programming
_______________________________

Explation: 
          Here while and else are keywords.
          
          Here test cond is either True or False
          
          If Test Cond is True then PVM Executes Indentation Block of statements and again PVM goes to Test cond, if 
          again Test cond is True then
          
          PVM executes indentation Block of statement. This process is repeated Finite number of times until Test cond 
          becomes False  
          
          Once Test cond becomes False then PVM Executes else block of statement (if present) and later executes othe 
          statement in program.'''

# Example:

# Write a python program which will generate one to n numbers where n is positive value.
n = int(input("Enter how Many number you want to Generate: "))
if n <= 0:
    print("{} is invalid input")
else:
    i = 1  # Initialization part
    while(i <= n):  # Cond part
        print(i)
        i = i + 1  # Updation Part
    print("___________________________________")


# Write a python program which will generate n to one numbers where n is positive value.
n = int(input("Enter how many Numbers you want to generate: "))
if n <= 1:
    print("{} is Invalid input".format(n))

else:
    i = n  # Initialization part
    while i >= 1:  # Cond part
        print(i)
        i = i - 1  # Updation Part
    else:
        print("---------------------------------")


# Write a python program which will generate Even numbers within n, where n is positive value.
n = int(input("Enter how many Numbers you want to generate: "))
if n <= 1:
    print("{} is Invalid input".format(n))

else:
    i = 2  # Initialization part
    while i <= n:  # Cond part
        print("\t{}".format(i))
        i = i + 2  # Updation Part
    else:
        print("---------------------------------")


# Write a python program which will generate Odd numbers within n, where n is positive value.
n = int(input("Enter how many Numbers you want to generate: "))
if n <= 1:
    print("{} is Invalid input".format(n))

else:
    i = 1  # Initialization part
    while i <= n:  # Cond part
        print("\t{}".format(i))
        i = i + 2  # Updation Part
    else:
        print("---------------------------------")


# Write a python program which will generate Multiplication Table for the given positive integer value.
n = int(input("Enter how many Numbers you want to generate: "))
if n <= 1:
    print("{} is Invalid input".format(n))

else:
    i = 1  # Initialization part
    while i <= 10:  # Cond part
        mul = n * i
        print("{} * {} = {}".format(n, i, mul))
        i = i + 1  # Updation Part
    else:
        print("---------------------------------")

#                           OR

# n = int(input("Enter a Mul Table:"))
if(n <= 0):
    print("{} is invalid Input".format(n))
else:
    print("========================")
    print("Mul Table for :{}".format(n))
    print("========================")
    i = 1
    while(i<=10):
        print("\t{} x {} = {}".format(n, i, n*i))
        i=i+1
    else:
        print("========================")


# Write a python program which will find the sum of n natural numbers.
n = int(input("Enter how Many number you want Add: "))
if n <= 0:
    print("{} is invalid input")
else:
    s = 0
    i = 1
    while i <= n:
        print(i)
        ss = ss + i
        i = i + 1
    else:
        print("----------------------------------------")
        print("Sum = {}".format(s))
        print("----------------------------------------")


# Write a python program which will find the sum of Squares of n natural numbers.
n = int(input("Enter How Many Numbers Squares Sum u want to find:"))
if(n <= 0):
    print("{} is Invalid Input".format(n))
else:
    print("--------------------------------------")
    print("Nat Numbers Squares Sum within {}".format(n))
    print("--------------------------------------")
    ss = 0  # Additive Identity--to keep tarck temp Sum
    i = 1
    while(i <= n):
        print("\tSquare,Circle({}) = {}".format(i, i**2))
        ss = ss + i ** 2
        i = i + 1
    else:
        print("=============================")
        print("Squares Sum = {}".format(ss))
        print("=============================")


# Write a python program which will find the sum of Cubes of n natural numbers.
n = int(input("Enter How Many Numbers Squares Sum u want to find:"))
if(n <= 0):
    print("{} is Invalid Input".format(n))
else:
    print("--------------------------------------")
    print("Nat Numbers Cubes Sum within {}".format(n))
    print("--------------------------------------")
    c = 0  # Additive Identity--to keep tarck temp Sum
    i = 1
    while(i <= n):
        print("\tSquare,Circle({}) = {}".format(i, i**3))
        c = c + i ** 3
        i = i + 1
    else:
        print("=============================")
        print("Cubes Sum = {}".format(c))
        print("=============================")


# Write a python program which will find the product of n natural numbers.
n = int(input("Enter How many numbers do U want the Product of:  "))
if n <= 0:
    print("{} is Invalid Input".format(n))

else:
    print("----------------------------------------------------------")
    print("Nat Numbers Product Within {}".format(n))
    print("----------------------------------------------------------")

    i = 1
    p = 1
    while(i <= n):

        p = p * i
        i = i + 1
        print("{}".format(p))
    else:
        print("---------------------------------")

# Program for Implementing string data
s = "HAVANA"
i = 0
while i < len(s):
    print("\t{}".format(s[i]))
    i = i + 1
print("________________________________________")

# For reversing the data
s = "HAVANA"
i = 0
while i < len(s):
    print("\t{}".format(s[i]))
    i = i + 1
print("________________________________________")


# Write a Python Program which will find Sum of first n natural numbers, Squares of n natural numbers and Cubes of n natural numbers.
n = int(input("Enter How Many Numbers Squares Sum u want to find:"))
if(n <= 0):
    print("{} is Invalid Input".format(n))
else:
    print("--------------------------------------")
    print("Nat Numbers  Sum within {}".format(n))
    print("--------------------------------------")
    print("Nat Nums\tSquares\tCubes")
    print("--------------------------------------")
    s, ss, cs=0, 0, 0 # Additive Identity--to keep tarck temp Sum
    i = 1
    while(i <=n ):
        print("\t{}\t\t{}\t\t{}".format(i,i**2,i**3))
        s = s + i
        ss = ss + i ** 2
        cs = cs + i ** 3
        i = i + 1
    else:
        print("=============================")
        print("\t{}\t\t{}\t\t{}".format(s,ss,cs))
        print("=============================")

# Write a python programm which will cal Factorial of a given number.
n = int(input("Enter Number for cal Factorial: "))
if n < 0:
    print("{} is Invalid Input".format(n))

else:
    print("----------------------------------------------------")
    print("Factorial numbers within {}".format(n))
    print("----------------------------------------------------")
    i = 1
    f = 1
    while i <= n:
        f = f * i
        i = i + 1
    else:
        print("Factorial({}!) = {}".format(n, f))








