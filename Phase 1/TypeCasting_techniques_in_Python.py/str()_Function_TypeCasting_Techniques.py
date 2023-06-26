#str() is used to cnvert all type of all Type of values into str value.
#Syntax: varname=str(int / float / bool / complex)

#Example1. : int type to str
a = 100
print(a,type(a)) # 100 <class 'int'>
b = str(a)
print(b,type(b)) # 100 <class 'str'>


#Example2. : float type to str
a = 23.945
print(a,type(a)) # 23.945 <class 'float'>
b = str(a)
print(b,type(b)) # 23.945 <class 'str'>



#Example3. : bool type to str
a = True
print(a,type(a)) # True <class 'bool'>
b = str(a)
print(b,type(b)) # True <class 'str'>



#Example4. : complex type to str
a = 28+300j
print(a,type(a)) # (28+300j) <class 'complex'>
b = str(a)
print(b,type(b)) # (28+300j) <class 'str'>







