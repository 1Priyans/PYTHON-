# Relational Operators (Comparison Operators)

__Properties = '''The purpose of Relational Operators is that "To Compare Two  Values".
=>If two values / Objects connected with Relational Operators then it is called Relational Expression".
=>The result of Relational Expression is either True or False.
=>The Relational Expression is also called Test Condition.
=>In Python Programming, we have 6 Types of Relational operators. They are given in the following Table.
===============================================================================
SLNO		SYMBOL			MEANING		EXAMPLE
===============================================================================
1.			>				greater than		print(10>5)-----------True
											print(10>20)----------False
2.			<				less than			print(10<20)----------True
											print(10<5)-----------False

3.			==				Equality Operator	print(10==20)--------False
							(double equal to)	print(10==10)--------True

4.			!=				not equal to		print(10!=20)--------True
											print(10!=10)--------False

5.			>=				greater than		print(10>=10)------True
							or equal to		print(10>=20--------False

6.			<=				less than			print(10<=10)------True
							or equal to		print(10<=5)------False
=================================================================================='''

# Write a Python Program which will demonstrate Relational operators
# a = int(input("Enter the Value of a: "))
# b = int(input("Enter the Value of b: "))
# print("\tRelational Operators")
# print("*"*80)
# print("\t {} > {} = {}".format(a,b,a>b))
# print("\t {} < {} = {}".format(a,b,a<b))
# print("\t {} == {} = {}".format(a,b,a==b))
# print("\t {} != {} = {}".format(a,b,a!=b))
# print("\t {} >= {} = {}".format(a,b,a>=b))
# print("\t {} <= {} = {}".format(a,b,a<=b))
# print("*"*80)

# Example:
print("python" > "python")  # False (Same Values then false)

print("PYTHON" > "python")  # False
print(ord("P")) # 80
print(ord("p")) # 112

# NOTE:  ord() is pre-defined Function which gives UNICODE Value for any Alphabet ,Symbols, and digits
print((ord("p")) + (ord("y")) + (ord("t")) + (ord("h")) + (ord("o")) + (ord("n")))  # 674
print((ord("P")) + (ord("Y")) + (ord("T")) + (ord("H")) + (ord("O")) + (ord("N")))  # 482

# NOTE: chr() is pre-defined Function which gives  Alphabet ,Symbols, and digits for UNICODE Value.
print(chr(65))  # A
print(chr(68))  # D
print(chr(69))  # E

print("INDIA" > "INDIA")  # False
print("INDIA" > "INDAI")  # True  Here IA = AI, I is greater then A

print("PYTHON" >= "PYTHON"[::-1])  #  True # here "PYTHON" >= "NOHTYP"
print("MADAM" >= "MADAM"[::-1])  # True

print("@#$%" > "&*(#")  # True
print(ord("@"))  # 64

print("1234" > "4321")  # False
print(chr(4))  # 
print(chr(48)) # 0