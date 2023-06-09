# 5. Bitwise Operator
__Properties = '''1) The Bitwise Operators are applicable on Integer data but not on Floating Point Values bcoz floating point values does not 
                     contain Certainty.

2) Bitwise Operators are used for Performing Operations on Integer data in the form of Bit by Bit. 

3)In otherwords, Bitwise operators First Converts Integer data into Binary Format and Performs operations on Binary Data in the form of Bit by Bit. 
  Since these Operators are performing Bit by Bit on Integer Binary data and hence They named as Bitwise Operators.

3) In Python Programming, we have 6 Bitwise Operators. They are given in the following Table.
=========================================================================
SLNO	SYMBOL			MEANING		
=========================================================================
1.		<<				Bitwise Left Shift Operator
2.		>>				Bitwise Right Shift Operator
3.		|				Bitwise OR Operator
4.		&				Bitwise AND Operator
5.		~				Bitwise Complement Operator
6.		^				Bitwise XOR Operator
========================================================================= '''


# 1 Bitwise Left Shift Operator
__Properties = '''         Syntax:  varname=GivenNumber << No. of Bits

Concept: The Bitwise Left Shift Operator ( << )  shifts No. of Bits Towards Left Side By adding No. of Zero at Right Side (depends on No. of Bits). 
            So that result value will displayed in the form of decial number system. '''

# Example:
a = 4
b = 2
c = a << b  # res = Given number << No of Bits  # res = Given no * 2 (to the power of No. of Bots)
print(c, type(c))  # 16 <class 'int'>

a = 6
b = 2
c = a << b
print(c, type(c))  # 24 <class 'int'>


# 2 Bitwise Right Shift Operator
__Properties = '''         Syntax:  varname=GivenNumber >> No. of Bits

Cocept: The Bitwise Right Shift Operator ( >> )  shifts No. of Bits Towards Right Side By Adding No. of Zero at Left  Side (depends on No. of Bits) 
        result value will displayed in the form of decimal number system.'''

# Example:
a = 4
b = 3
c = a >> b
print(c, type(c))  # 0

a = 10
b = 3
c = a >> b  # res = Given number >> No of Bits  # res = Given no / 2 (to the power of No. of Bots)
print(c)  # 1 (bcoz Bitwise Operator does not support floating point values so it will be solve like '10//8 = 1' Which is called as Floor Division

print(25 >> 4)  # 1

print(24 >> 3)  # 3

print(50 >> 4)  # 3

print(45 >> 2)  # 11


# 3 Bitwise OR Operator:
__Properties = '''              Syntax:    varname=Val1 | Val2

1) The Functionality of Bitwise OR Operator is expressed by using the following Truth Table
===================================================
	Val1		Val2		Val1 | Val2
====================================================
	  0		     0			    0
	  1	         0 			    1
	  0		     1			    1
	  1		     1			    1
==================================================== '''

# Example:
print(0 | 0)  # 0
print(1 | 0)  # 1
print(0 | 1)  # 1
print(1 | 1)  # 1

print(False | False)  # False
print(False | True)   # True
print(True | False)   # True
print(True | True)    # True

a = 10
b = 12
c = a | b  # here 10--> 1010, 12--> 1100 now 1010 | 1100 = 1110 in decimal its 14
print(c)  # 14

print(10 | 15)  # 15

print(3 | 4)  # 7

s1={10, 20, 30}
s2={15, 20, 35}
s3 = s1.union(s2)
print(s3,type(s3))  # {35, 20, 10, 30, 15} <class 'set'>

s4 = s1 | s2
print(s4, type(s4)) # {35, 20, 10, 30, 15} <class 'set'>

s1 = {"Apple", "Mango", "Kiwi"}
s2 = {"Sberry", "Apple", "Guava"}
s3 = s1.union(s2)
print(s3, type(s3))  # {'Mango', 'Guava', 'Sberry', 'Kiwi', 'Apple'} <class 'set'>

s4 = s1 | s2  # Bitwise OR Operator
print(s4, type(s4))  # {'Mango', 'Guava', 'Sberry', 'Kiwi', 'Apple'} <class 'set'>


# Special Ponits
print(100 or 200)  # 100  "First value 100 Bcoz 100 is non zero value so it is true 100 will be the output we get and it is short cicuit Evaluation is well"

print(-123 or 400) # -123 # First Value

print(123 or 0)  # 123  # First Value

print(0 or 123)  # 123 Second  Value

print(3 | 4)  # 7

print(3 or 4)  # 3 First Value

print(0 or 234 or 0 or 34)  # 234 Second Value

print(100 and 200)  # 200 When first value is True then its not going to other condition so 200

print(100 and 0)  # 0
print(100 and -123)  # -123
print("KVR" or "PYTHON")  # "KVR"
print("KVR" or "PYTHON" or False)  # "KVR"
print(False or "KVR" or "PYTHON" or False)  # "KVR"
print("KVR" and "PYTHON")  # "PYTHON"
print("KVR" and 567)  # 567


print(100 and 200 or 456)  # 200
print(100 and 200 or 567 or "KVR" and 450 and 678)  # 200
print(100 & 200)  # 64
print(100 and 200)  # 200
print("$" and "%" or 123)  # "%"

# 4 Bitwise AND Operator:
___Properties = '''             Syntax:    varname=Val1 & Val2

1) The Functionality of Bitwise AND Operator is expressed by using the following Truth Table
		======================================================================
			Val1		Val2		    Val1 & Val2
		======================================================================
			 0		     0			        0	
			 1		     0		        	0
			 0		     1			        0
			 1		     1			        1
		====================================================================== '''

# Example:
print(0 and 0)  # 0
print(1 and 0)  # 0
print(0 and 1)  # 0
print(1 and 1)  # 1

a = 14
b = 13
c = (a & b)  # Here 14--> 1110, 13-->1101(binary form) so here 1110 and 1101----> 1100 which is 12
print(c, type(c))  # 12 <class 'int'>

print(10 and 15)  # 10

print(3 & 4)  # 0

print("Keshav" and "Regular" and "Forgot")  # "Forgot"

print(bin(4))

# 5. Bitwise Complement Operator
_Properties = '''           Syntax:-     varname=~value

1) The Functionality of Bitwise Complement Operator ( ~ ) is that "It Inverts the bits".

2) Inverting the Bits are nothing but 0 becomes 1 and 1 becomes 0.

3) The Formula for Bitwise Complement Operator ( ~ ) is that " ~Value= - (Value+1)'''

# Example:
a = 12
c = (~ a)  # here is 12---> 1100 and formula is -(value + 1) i.e. -(1100 or 0001) so result is 1101(bin) which is -13
print(c, type(c))  # -13 <class 'int'>
print(a)  # 12

# 6. Bitwise XOR Operator
____Properties = '''        Syntax:    varname = Val1 ^ Val2

1) The Functionality of BitwiseXOR Operator is expressed by using the following Truth Table
===============================================================
		  Val1		     Val2		Val1 ^ Val2
===============================================================
			0		      0			     0	
			1		      0			     1
			0		      1			     1
			1		      1			     0
=============================================================== '''

# Example:
print(0 ^ 0)  # 0
print(0 ^ 1)  # 1
print(1 ^ 0)  # 1
print(1 ^ 1)  # 0

a = 4
b = 2
c = (a ^ b)  # here 4-->0100, 2-->0010 now, (0100 '^' XOR  0010 = 0110) which is 6
print(c, type(c))  # 6 <class 'int'>
print(b, type(b))  # 2 <class 'int'>
print(a, type(a))  #4 <class 'int'>

print(4 ^ 5)  # 1

print(10 ^ 5)  # 15

s1 = {10, 20, 30}
s2 = {15, 20, 25}
print(s1,type(s1))  # {10, 20, 30} <class 'set'>
print(s2,type(s2))  # {25, 20, 15} <class 'set'>

s3 = s1.symmetric_difference(s2)
print(s3, type(s3))  # {10, 15, 25, 30} <class 'set'>

s4 = (s1 ^ s2)  # Bitwise XOR

print(s4, type(s4))  # {10, 15, 25, 30} <class 'set'>


