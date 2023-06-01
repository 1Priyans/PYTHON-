# Python Ternary Operator
__Properties = ''' The Ternary Operator in Python Programming Language is " if .. else Operator ".

Syntax:       varname =  Expr1  if Test Cond else Expr2 

Explanation:
--------------
a) Here "if" and "else" are the keywords

b)Here Test Cond is to be evaluated either to be True or False

c)If the Test Condition is True then PVM Executes Expr1 and whose Result assigned to Varname

d)If the Test Condition is False then PVM Executes Expr2 and whose Result assigned to Varname

e)Hence varname contains result of either Expr1 or Expr2 '''

# Write a python program which will accept two numerical values and find the biggest among them by using Ternary Operators and check for equality.
a = float(input("Enter First Value: "))
b = float(input("Enter Second Value: "))

bval = a if a > b else b

bval1 = a if a > b else b if b > a else "Both Values are Equal"

print("Big ({}, {} = {})".format(a, b, bval))
print("Big ({}, {} = {})".format(a, b, bval1))


# Write a python program which will accept two numerical values and find the Smallest among them by using Ternary Operators and check for equality.
a = float(input("Enter First Value: "))
b = float(input("Enter Second Value: "))

smval = a if a < b else b

smval1 = a if a < b else b if b < a else "Both Values are Equal"

print("Small ({}, {} = {})".format(a, b, smval))
print("Small ({}, {} = {})".format(a, b, smval1))


# Write a python program which will accept any word or Value and decide weather it is Palindrome or not.
word = input("Enter any Word/Value: ")
res = "PALINDROME" if word.upper() == word[::-1].upper() else "Not PALINDROME"
print("{} is {}".format(word, res))


# Write a python program which will accept a word and decide weather it is Vowel word or not
word = input("Enter any Word: ").lower()
res = "Vowel Word" if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word else "Not vowel Word"
print("{} is {}".format(word, res))


# Write a python program which will accept the number which is even or odd
num = int(input("Enter any Number: "))
res = "Even Number" if (num % 2 == 0) else "Odd Number"
print("{} is {}".format(num, res))


