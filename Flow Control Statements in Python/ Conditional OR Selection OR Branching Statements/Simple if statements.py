# 1. Simple if statements
___Properties = '''
Syntax :

if (Test Cond):
-----> Statement 1
-----> Statement 1
-----> ___________
-----> Statement-n
---------------------------
Other Statements in Programming
____________________________

Explanation: Here if and else are keywords 
             If Test Cond is True then PVM Executes Indentation Block of statements 1  and later executes other statements.
             If the Test Cond is False then PVM Executes  Indentation block of statements 2 and later executes Other statements in program.'''

# Example:

# Write a python program which will three numerical integer values and decide the biggest among them and check for the Equality.
num1 = int(input("Enter First Value: "))
num2 = int(input("Enter Second Value: "))
num3 = int(input("Enter Third Value: "))
if (num1 >= num2) and (num1 >= num3):
    print("{} is Biggest numerical Value".format(num1))

if (num2 > num1) and (num2 >= num3):
    print("{} is Biggest numerical Value".format(num2))

if (num3 >= num1) and (num3 > num2):
    print("{} is Biggest numerical Value".format(num3))

if (num1 == num2) and (num2 == num3) and (num3 == num1):
    print("All Value are Equal")


# Write a python program which will accept any digits and print the name of the digits.
d = int(input("Enter any Digit:"))   # d= 0 1 2 3 4 5 6 7 8 9  123
if(d == 0):
    print("{} is ZERO".format(d))
if(d == 1):
    print("{} is ONE".format(d))
if(d == 2):
    print("{} is TWO".format(d))
if(d == 3):
    print("{} is THREE".format(d))
if(d == 4):
    print("{} is FOUR".format(d))
if(d == 5):
    print("{} is FIVE".format(d))
if(d == 6):
    print("{} is SIX".format(d))
if(d == 7):
    print("{} is SEVEN".format(d))
if(d == 9):
    print("{} is NINE".format(d))
if(d == 8):
    print("{} is EIGHT".format(d))
if(d in [-1, -2, -3, -4, -5, -6, -7, -8, -9]):
    print("{} is -Ve Digit".format(d))
if(d not in [-1, -2, -3, -4, -5, -6, -7, -8, -9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print("{} is a Number:".format(d))
print("Program execution completed")


#Write a python program which will accept any numerical value and decide weather it is even or odd.
num = int(input("Enter Any Number: "))
if (num % 2 == 0):
    print("{} is Even".format(num))
if (num % 2 != 0):
    print("{} is Odd".format(num))
print("Program Execution Completed")


#Write a python program which will accept any word or Value and decide weather it is Palindrome or not.
word = input("Enter Any Word or Value: ")
if word.upper() == word[::-1].upper():
    print("{} is Palindrome".format(word))
if word.upper() != word[::-1].upper():
    print("{} is not Palindrome".format(word))


#Write a python program which will accept any numerical value and decide weather it is Positive or Negative or Zero.
num = float(input("Enter Any Numerical Value: "))
if (num > 0):
    print("{} is POSITIVE NUMBER".format(num))
if (num < 0):
    print("{} is NEGATIVE NUMBER".format(num))
if (num == 0):
    print("{} is ZERO".format(num))
print("Program Execution Completed")