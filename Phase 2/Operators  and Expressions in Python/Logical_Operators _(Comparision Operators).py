# 4. Logical Operators (Comparison Operators)

__Properties = '''1) The purpose of Logical Operators is that "To compare the result of Two or More Relational 
                     Expressions".

2)If Two or More Relational Expressions are connected with Logical Operators then It is called Loogical 
    Expressions.

3)The result of Logical Expressions is either True or False.

4)The Logical Expressions is also called Compound Condition (More than one Test Cond).

5)In Python Programming, we have 3 Logical Operators. They are given in the following Table.
=================================================================================
SLNO		SYMBOL			MEANING			
=================================================================================
1.			and				Physical ANDing		
2.			or				Physical ORing
3.			not				---------------------------
================================================================================= '''

# a) 'and' Operator ( Physical ANDing ):
_Properties = '''       Syntax:   RelExpr1 and RelExpr2

The Functionality of "and" Operators described by using the following Truth table.
===================================================================
		RelExpr1		RelExpr2		RelExpr1 and RelExpr2
===================================================================
		True		    False				False		
		False	        True				False
		False	        False				False
		True		    True				True
=================================================================== '''
# Examples:
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
print(True and True)  # True

print((10 > 20) and (20 > 10))  # False (Short Circuit Evaluation)

print((10 > 5) and (20 > 30) and (40 > 30))  # False (Short Circuit Evaluation)

print((10 > 5) and (20 > 10) and (30 > 4))  # True (Full length Evaluation)
_Note = ''' Short Circuit Evaluation of "and" operator:

If Two or More Relational Expressions are connected with "and" operator and If the First relational Expression is False then PVM Will not evalute 
Rest of the Relational Expressions and The result of entire Logical Expressions is False. This Process of Evalulation is called Short Circuit 
Evaluation.'''


# b) "or" Operator (Physical ORing)
__Properties = '''      Syntax:   RelExpr1 or RelExpr2

The Functionality of "or" Operators described by using the following Truth table.
======================================================================
		RelExpr1		RelExpr2		RelExpr1 or RelExpr2
======================================================================
		 True		     False				True	
		 False	         True				True
		 False	         False				False
		 True		     True				True
========================================================================'''

# Example:
print(10 > 20 or 20 > 30 or 30 > 10)  # True (Full length Evaluation)

print(10 > 5 or 20 > 30 or 40 > 50)  # True (Short Circuit Evaluation)

print(10 > 20 or 20 > 10 or 40 > 50)  # True (Short Circuit Evaluation)

print(10 > 20 or 20 > 100 or 40 > 50)  # False (Full length Evaluation)
_Note ='''Short Circuit Evaluation of "or" operator
        
          If Two or More Relational Expressions are connected with "or" operator and If the First relational Expression is True then PVM Will 
not evaluate Rest of the Relational Expressions and The result of entire Logical Expressions is True. This Process of Evalulation is called Short 
Circuit Evaluation.'''


# c). "not" Operator
__Properties = '''      Syntax:   not RelExpr1 

The Functionality of "or" Operators described by using the following Truth table.
=======================================================
		      RelExpr1		not RelExpr1		
========================================================
			    True		   False			
			    False		   True				
========================================================'''
# Example:
a = True
print(a)  # True
print(not a)  # False

b = False
print(b)  # False
print(not b)  # True

print(10 > 20)  # False
print(not 10 > 20)  # True

print(not 10 != 20)  # False

print(not 10 == 20)  # True

print(1234)  # 1234
# print(not 1234)  # False  1234 is non zero value so True but its (not  1234) so its False

print("MAVERICK")  # MAVERICK
print(not "MAVERICK")  # False  "MAVERICK" is non zero value so True but its (not  MAVERICK) so its False

print(not 0)  # True
print(not .0000000000000000000000000000000000000003)  # False

print(not "")  # True
print(not "  ")   # False