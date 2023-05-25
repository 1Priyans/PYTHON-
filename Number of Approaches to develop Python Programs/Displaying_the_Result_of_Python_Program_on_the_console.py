__Proprties = '''1) To Display  the Result of Python Program on the console, we use print()

2)In Otherwords, print() is one of the pre-defined function is used Displaying  the Result of Python 
    Program on the console.

3)we can use print() with the following syntaxes
                
Syntax-1  : print(Value)
			            
                        (OR)
		   
            print(Value1,Value2,....Value-n)

With this syntax we can display either single or Multiple Values.'''

#Examples:
a = 12
b = 13
print(a) # 12
print(b) # 13

a = 20
b = 30
c = a+b
print(a, b, c) # 20 30 50

_Properties = '''Syntax-2:   print(Msg)
			            
                                    (OR)
		  
                            print(Msg1,Msg2,...Msg-n)
			                        
                                    (OR)
		
                            print(Msg1+Msg2+....+Msg-n)
                            
a)Here Msg1,Msg2...Msg-n are Str type values

b)This Syntax displays Str Values'''

#Example:
a = 'Python Programming Environment'
print(a) # Python Programming Environment

a = 'Python'+'Programming'+'Environment'
print(a) # PythonProgrammingEnvironment

a = "Python", "Programming", "Environment"
print(a) # ('Python', 'Programming', 'Environment')

a = 'Python'+" "+'Programming'+" "+'Environment'
print(a) # Python Programming Environment

# print("Hello"+10) # TypeError: can only concatenate str (not "int") to str

print("Hello"+"10") # Hello10
print("Hello"+" "+"10") # Hello 10

print("1"+"2"+"3") # 123

print(str(1.34)+" "+str(2.45)+" "+str(3.56)) # 1.34 2.45 3.56


_Properties = '''   Syntax-3: print(Messages cum Values)
			                    
                                        (OR)
		
                            print(Values Cum Message)

This Syntax generates / Displays Message Cum Values '''

#Example:
a = 10
#value of a is 10 and it is greater then 9
print("Value of a is", a, "and it is greater then 9") # Value of a is 10 and it is greater then 9

a = 10
b = 20
c = a+b
#Value of a = 10
print("Value of a =", a) # Value of a = 10

name = "Guido van Russom"
print(name) # Guido van Russom

#Guido van Russsom is Devloper of Python Programming language
print(name, "is Devloper of Python Programming language")#Guido van Russom is Devloper of Python Programming language


_Properties = '''  Syntax-4: print(Messages Cum Values with format()) 

This Syntax generates / Displays Message Cum Values  by using format()'''

#Example:
a = 100
#Value of a is 100
print("Value of a is {}".format(a)) # Value of a is 100

#Value of a is 100 and it is greater then 99 
print("Value of a is {} and it is greater then 99".format(a)) # Value of a is 100 and it is greater then 99

a = 200
b = 300
c = a+b
#Sum of 200 and 300 = 500
print("Sum of {} and {} = {}".format(a,b,c)) # Sum of 200 and 300 = 500

a = 200
b = 300
c = a+b
#sum of  200 , 300  and  200 = 500
print("sum of {}, {} and {} = {}".format(a,b,a,c)) # sum of 200, 300 and 200 = 500


_Properties = '''  Syntax-5: print(Messages Cum Values with format specifiers 

a) This Syntax generates / Displays Message Cum Values  by using format specifiers

b) In Python Programming, For Displaying Integer Data, we use %d format specifier.

c)For Displaying Float Data, we use %f format specifier.

d) For Displaying str Data, we use %s format specifier.
						
NOTE: if any value / data does not contain format specifier then we must convert that values / 
      data into str type by using str() '''

#Example:
a = 1000
#Value of a is 1000
print("Value of a is %d" %a) # Value of a is 1000

a = 200
b = 300
c = a+b
#sum of  200 , 300  and  500 = 300
print("sum of %d, %d, and %d = %d" %(a,b,c,b)) # sum of 200, 300, and 500 = 300

a = 100
#Value of a is 100 and it is greater then 99 
print("Value of a is %d and it is greater then 99" %a) # Value of a is 100 and it is greater then 99

a = 10
b = 20.34
c = "Python"
#sum of 10 and 20.340000 = Python
print("sum of %d and %f = %s" %(a,b,c)) # sum of 10 and 20.340000 = Python

#sum of 10 and 20.34(when two decimal places are required) = Python
print("sum of %d and %.2f = %s" %(a,b,c)) # sum of 10 and 20.34 = Python

a = 10
name = "Russom"
marks = 22.22
#My Number is 10 and Name is Rossum and marks=22.22
print("My Number is %d and name is %s and marks = %.2f"%(a,name,marks)) # My Number is 10 and name is Russom and marks = 22.22

lst=[10,"Rossum",33.34,True,2+3j]
print("Content of List",lst) # Content of lst= [10, 'Rossum', 33.34, True, (2+3j)]

print("Content of List = {}".format(lst)) # Content of List = [10, 'Rossum', 33.34, True, (2+3j)]

print("Content of List = %s" %str(lst)) # Content of List = [10, 'Rossum', 33.34, True, (2+3j)]

d={10:"Apple",20:"Mango"}
#Content of d= {10: 'Apple', 20: 'Mango'}
print("Content of d =",d)

#Content of d= {10: 'Apple', 20: 'Mango'}
print("Content of d = {}".format(d)) 

#Content of d= {10: 'Apple', 20: 'Mango'}
print("Content of d = %s" %str(d))


_Properties = '''  Syntax-6: print(Values, end= )

This Syntax display the values Horizontally (Same Line) end with specified Symbols'''

#Example:
a = range(1,11)
print(a,type(a)) # range(1, 11) <class 'range'>

for b in a:
    print(b)
#This is the Output we got
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

#for displaying the values Horizontally
# for b in a:
#     print(b,end=" ") # 1 2 3 4 5 6 7 8 9 10

# for b in a:
#     print(b,end="----->")# 1----->2----->3----->4----->5----->6----->7----->8----->9----->10----->


#Special Point:
lg = "Python"
print(lg,type(lg)) # Python <class 'str'>
lg = lg+lg+lg
print(lg,type(lg)) # PythonPythonPython <class 'str'>

lg = lg + lg+ lg
print(lg,type(lg)) # PythonPythonPythonPythonPythonPythonPythonPythonPython <class 'str'>

lg = "Python"
print(lg,type(lg)) # Python <class 'str'
lg = 3*lg # here * operator is called Repetation Operator
print(lg,type(lg)) # PythonPythonPython <class 'str'>

lst=[20.34, 34, "Rossum"] 
print(lst,type(lst)) # [20.34, 34, 'Rossum'] <class 'list'>
lst = 4*lst # # here * operator is called Repetation Operator
print(lst,type(lst)) # [20.34, 34, 'Rossum', 20.34, 34, 'Rossum', 20.34, 34, 'Rossum', 20.34, 34, 'Rossum'] <class 'list'>

print("=") # =

print(50*"=") # ==================================================
 
print(50*"*") # **************************************************

print(1000*3) # Here * is called Mul Operator # 3000

# print("12"*"3") # TypeError: can't multiply sequence by non-int of type 'str'

print("23"*10) # 23232323232323232323

print("*"*5) # *****

for val in range(11):
    print("*")