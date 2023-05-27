# 2. Assignment Operator
__Properties = '''1) The purpose of assignment operator is that " To assign or transfer Right Hand Side (RHS) Value / Expression Value to the 
                     Left Hand Side (LHS) Variable "

2) The Symbol for Assignment Operator  is single equal to ( = ).

3)In Python Programming,we can use Assigment Operator  in two ways.
				a) Single Line Assigment
				b) Multi Line Assigment 

a) Single Line Assignment:  Syntax: LHS Varname= RHS Value

			                        LHS Varname= RHS Expression

With  Single Line Assignment at a time we can assign one RHS Value / Expression to the single LHS Variable Name.'''

# Example:
# a = 23
# b = 24
# c = 26
# print(a,b,c)

__Properties = '''b) Multi Line Assigment: Syntax: Var1,Var2.....Var-n= Val1,Val2....Val-n

			                                       Var1,Var2.....Var-n= Expr1,Expr2...Expr-n

1) Here The values of Val1, Val2...Val-n are assigned to Var1,Var2...Var-n Respectively.

2)Here The values of Expr1, Expr2...Expr-n are assigned to Var1,Var2...Var-n Respectively.'''

# Example:
# a, b = 100, 200
# add, sub, mul = a+b, a-b, a*b
# print(add, sub, mul) # 300 -100 20000
#
# lst, tpl = ["Russom", 1991, "PYTHON" ], ("Travis", 1981, "Java")
# print(lst,type(lst))  # ['Russom', 1991, 'PYTHON'] <class 'list'>
# print(tpl,type(tpl))  # ('Travis', 1981, 'Java') <class 'tuple'>
#
# a, b = 100, 200 # Called Swapping logic
# print(a, b) # 100 200
# a, b = b, a
# print(a,b) # 200 100

# Write a Python Program which will accept any two values and interchange or Swap them.
# a = input("Enter the Value of a: ")
# b = input("Enter the Value of b: ")
# print("Original Value of a = {}".format(a))
# print("Original Value of b = {}".format(b))
# a,b = b,a # Swapping Logic # Multi Line assignment
# print("*"*80)
#
# print("Swapped Value of a = {}".format(a))
# print("Swapped Value of b = {}".format(b))
#
# print("*"*80)


# 3. Relational Operators ( Comparison Operators)
