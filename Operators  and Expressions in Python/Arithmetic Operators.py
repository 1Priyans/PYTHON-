# 1. Arithmetic Operators
__Properties = '''1) The purpose of Arithmetic Operators is that "To Perform Arithmetic Operations such as 
                     Addition,Substraction, Multiplications etc..".
2) If two or More Objects OR Values Connected with Arithmetic Operators then we call it as Arithmetic 
   Expression.

Python Programming Contains 7 Arithmetic Operators. They are given in the following Table

---------------------------------------------------------------------------------------------------------------------------------------------
SLNO	SYMBOL			MEANING		EXAMPLE     a=10  b=3
---------------------------------------------------------------------------------------------------------------------------------------------
1.			+			Addition			print(a+b)---->13

2.			-			Substraction		print(a-b)----->7

3.			*			Multiplication		print(a*b)----->30

4.			/			Division			print(a/b)------>3.3333333333333335
					    (float Quotient)

5.			//			Floor Division		print(a//b)------>3
					     (Integer Quotient)

6.			%			Modulo Division	print(a%b)------>1
						(Remainder)

7.			**			Exponentiation	print(a**b)------>1000
---------------------------------------------------------------------------------------------------------------------------------------------'''

# Example:
# a = 21
# b = 5
# c = a+b
# print(a,b,c) # 21 5 26
# print(a+b) # 26
# print(a-b) # 16
# print(a*b) # 105
# print(a/b) # 4.2
# print(a//b) # 4
# print(a%b) # 1
# print(a**b) # 4084101
#
# print(100/5.0) # 20.0 # one no is float then we get output in the form of float point.
# print(100.0/5) # 20.0
#
# print(100/5.0) # 20.0
# print(100.0//5) # 20.0
# print(100//5) # 20
#
# print(100/5) # 20 # no one number in the the form of float then we get output in the form of integer type.
#
# print(10 / 3) # 3.3333333333333335
# print(10 // 3) # 3
#---------------------------------------------------------------------------------------------------------------------------------------------'''

# Write a Python Program which will demonstrate the functionality of Arithmatic Operators.
# a = int(input("Enter the value of a : "))
# b = int(input("Enter the value of b : "))
# print("*"*70)
# print("\tSum ({},{}) = {}".format(a,b,a+b))
# print("\tSub ({},{}) = {}".format(a,b,a-b))
# print("\tMul ({},{}) = {}".format(a,b,a*b))
# print("\tDivision ({},{}) = {}".format(a,b,a/b))
# print("\tFloor Division ({},{}) = {}".format(a,b,a//b))
# print("\tModulo Division ({},{}) = {}".format(a,b,a%b))
# print("\tExponentiation ({},{}) = {}".format(a,b,a**b))
# print("*"*70)

# Write a Python Program which will calculate the Square,Circle Root of the given number.
# num = int(input("Enter the value: "))
# sqrt = num**(1/2)
# sqrt1 = num**.5
# print("*"*60)
# print("Square,Circle Root of the given value = {}".format(sqrt))
# print("Square,Circle Root of the given value = {}".format(sqrt1))
# print("*"*60)

# Write a Python Program which will calculate the Cube Root of the given number.
# num = int(input("Enter the value: "))
# sqrt = num**(1/3)
# print("*"*60)
# print("Give value = {}".format(num))
# print("Square,Circle Root of the given value = {}".format(sqrt))
# print("*"*60)

# Write a Python Program which will calculate the Value of (a + b)**2 or (a + b)2
# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# binml = (a+b)**2
# binml1 = (a+b)*(a+b)
# print("*"*60)
#
# print("Value of a = {}".format(a))
# print("Value of b = {}".format(b))
# print("Value of (a+b)2 = {}".format(binml))
# print("Value of (a+b)2 = {}".format(binml1))
#
# print("*"*60)

# Write a Python Program which will calculate the Value of (a)m or a**m
# a = int(input("Enter the value of a: "))
# m = int(input("Enter the value of m: "))
# am = a**m
# print("*"*70)
#
# print("Value of a = {}".format(a))
# print("Value of m = {}".format(m))
# print("Value of (a)m = {}".format(am))
#
# print("*"*70)

# Write a Python Program which will calculate the Value of  a^m -^n
# a = int(input("Enter the value of a: "))
# m = int(input("Enter the value of m: "))
# n = int(input("Enter the value of n: "))
# val = a**(m-n)
# val1 = a**m/a**n
# print("*"*60)
#
# print("Value of a = {}".format(a))
# print("Value of m = {}".format(m))
# print("Value of m = {}".format(n))
# print("Value of a^m-^n  = {}".format(val))
# print("Value of a**m/a**n  = {}".format(val1))
#
# print("*"*60)

# Write a Python Program which will calculate the Simple Interest and Total amount of pay
p = float(input("Enter Principle Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time: "))
# To calculate  Simple Interest
si = (p*r*t)/100
# To calculate Total Amount
totalam = p + si

print("*"*80)
print("Simple Interest = {}".format(si))
print("Total Amount = {}".format(totalam))
print("*"*80)
