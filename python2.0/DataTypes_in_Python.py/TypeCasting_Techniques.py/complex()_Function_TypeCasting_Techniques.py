#complex() is used for converting one possible type value into complex type.
#Syntax: varname=complex(int / float / bool / str)

#Example1. : int type to complex--> Possible 
a = 200
print(a,type(a)) # 200 <class 'int'>
b = complex(a)
print(b,type(b)) # (200+0j) <class 'complex'>


#Example2. : float type to complex--> Possible
a = 56.432
print(a,type(a)) # 56.432 <class 'float'>
b = complex(a)
print(b,type(b)) # (56.432+0j) <class 'complex'>


#Example3. : bool type to complex--> Possible
a = True
print(a,type(a)) # True <class 'bool'>
b = complex(a)
print(b,type(b)) # (1+0j) <class 'complex'>
c = False
print(c,type(c)) # False <class 'bool'>
d = complex(c)
print(d,type(d)) # 0j <class 'complex'>


#Example4. : str type to complex 

#Case(a): Str int  into Complex-->Possible
a = "2340"
print(a,type(a)) # 2340 <class 'str'>
b = complex(a)
print(b,type(b)) # (2340+0j) <class 'complex'>

#Case(b): Str float into Complex-->Possible
a = "49.345"
print(a,type(a)) # 49.345 <class 'str'>
b = complex(a)
print(b,type(b)) # (49.345+0j) <class 'complex'>

#Case(c): Str bool into Complex--> Not Possible
a = "True"
print(a,type(a)) # True <class 'str'>
b = complex(a)
print(b,type(b)) #ValueError: complex() arg is a malformed string "Bcoz PVM takes 'True' as pure string"

#Case(d): Str complex into Complex-->Possible
a = "23+10j"
print(a,type(a)) # 23+10j <class 'str'>
b = complex(a)
print(b,type(b)) # (23+10j) <class 'complex'>

#Case(d): Str complex into Complex-->Possible
a = "PYTHON"
print(a,type(a)) # PYTHON <class 'str'>
b = complex(a)
print(b,type(b)) # ValueError: complex() arg is a malformed string




