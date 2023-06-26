_Properties = ''' 1.)'range' is one of the pre-defined class name and treated as Sequence Data Type.

2.)The Purpose of range data type is that "To maintain / Store range of Numerical Integer Values by 
    maintaining Equal Interval of Value(Step)." 

3.)An object of range allows us to perform Indexing and Slicing Operations.

4.)An object of range belongs to Immutable object bcoz 'range' object does not support item 
    assignment.

5.)In order to maintain range of values by using range data type, we use 3 Types of Syntaxes.
    a.)Syntax- range(value)  
    b.)Syntax- range(Start,Stop)  
    c.)Syntax- range(Start,Stop,Step) '''


#a.) Syntax- range(value)
# This Syntax generates of Range of Values from 0 to Value-1.
#Example: 
a = range(10)
print(a,type(a)) # range(0, 10) <class 'range'>
for val in a:
    print(val)
#This output we get
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# print(a[0]) # 0

for val in range(7):
    print(val)
#The Output we get
# 0
# 1
# 2
# 3
# 4
# 5
# 6

print(a[2])
for a in range(18)[::-1]:
    print(a)
a[0] = 100
print(a) # TypeError: 'int' object does not support item assignment "so this is immutable"


#b.)Syntax- range(Start,Stop)
#This syntax generates range of values from START to STOP-1 Values.
#Example:

a = range(0,10)
print(a,type(a)) # range(0, 14) <class 'range'>
# for val in a:
#     print(val)
#This Output we get
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
for val in a[::-1]:
    print(val)
#This Output we get
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
print(a[4]) # 4
for val in range(0,4):
    print(val)
# This Output we get
# 0
# 1
# 2
# 3
for val in range(-1,10):
    print(val)

for val in range(0,4):
    print(val,end=" ") # 0 1 2 3 For prnting horizontly

#In the above TWO Syntaxes, The deafult Step is 1 and it is Forward Direction.


#c.)Syntax- range(Start,Stop,Step)
#This syntax generates range of values from START to STOP-1 Values by maintaining Equal Interval of Value 
# in the form of STEP.
#Examples:

a = range(1,10,2)
print(a,type(a)) # range(1, 10, 2) <class 'range'>
for val in a:
    print(val) 
#This Output we get
# 1
# 3
# 5
# 7
# 9

for val in range(-10,0,1):
    print(val)
#This Output we get
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1
print(a[-1]) # 9



