# Anonymous OR Lambda Functions
___Properties = '''Anonymous Functions are those which does not contain any name explicitly (Un-known).

The purpose of Anonymous Functions is that " To Perform Instant Operations".

Instant Operations are those which are using at that point time only and no longer interested to re-use in other part 
of the project / application.

Anonymous Functions are containing single executable statement but not multiple executable statements.

Anonymous Functions automatically OR Implicitly returns the Result (no need to use return statement).

To Define Anonymous Functions, we use a keyword called "lambda" and Anonymous Functions are also called Lambda Functions.
----------------------------------------------------------------------------------------
Syntax:    varname=lambda params-list : Expression
-----------------------
Explanation
-----------------------
varname represents an object of type <class,'fucntion'>
lambda  is a keyword which is used for defining  Anonymous Function
params-list represents list of formal params which are used for storing Values coming from Function calls.
Expression reprsents single executable statement which provides logic for Instant Operations. Here PVM executes single  
executable statement and whose result returns Automatically / Implcitily (no need use to return statement)
----------------------------------------------------------------------------------------------------------------------'''

# Exmaple

# Program for Define a Function for addition of three numbers by using Anonymous function
addition = lambda a, b, c: a + b + c  # Single Executable Statement
# Main Program
res = addition(100, 200, 300)
print("Addition of a + b + c = {}".format(res))

# Program for Define a Function which will accept any three numbers and find the addition among them by using Anonymous function
addition = lambda a, b, c: a + b + c  # Single Executable Statement
# Main Program
a, b, c = float(input("Enter First Value: ")), float(input("Enter Second Value: ")), float(input("Enter Third Value: "))
res = addition(a, b, c)
print("Addition of {} + {} + {} = {}".format(a, b, c, res))


# Write a Python Program which will accept two numerical integer values and find the biggest among them and find the Equality as well by using anonymous function.
bignum = lambda a, b: a if a > b else b if b > a else "Both Values are Equal"
# Main Program
a, b = float(input("Enter First Value: ")), float(input("Enter Second Value: "))
res = bignum(a, b)
print("Biggest Value = {}".format(res))


# Write a Python Program which will accept three numerical integer values and find the biggest among them and find the Equality as well by using anonymous function.
bignum = lambda a, b, c: a if a > b else b if b > c else c if c > a else a or c
# Main Program
a, b, c = float(input("Enter First Value: ")), float(input("Enter Second Value: ")), float(input("Enter Third Value: "))
res = bignum(a, b, c)
print("Biggest Value = {}".format(res))


# Write a Python Program which will find weather the given word or Value is PALINDROME or NOT by using Anonymous Function
palindrom = lambda word: "PALINDROME" if word == word[::-1] else "Not PALINDROME"
# Main Program
word = input("Enter the Value or Word for Which is Palindrome or Not: ").upper()
res = palindrom(word)
print("{} is {}".format(word, res))


# Write a Python Program which will accept a word and Decide weather it is Vowel word or not by using Anonymous Function.
vowl = lambda word: "Vowel Word" if word == "a" or word == "e" or word ==  "i" or word == "o" or word == "u" else "Not Vowel Word"
# Main Program
word = input("Enter Any Word for which the Word is Vowel word or Not: ").lower()
res = vowl(word)
print("{} is {}".format(word, res))


# Write a python programm which will accept list of numerical values and find the maximum and minimum by using Anonymous Funtion.









