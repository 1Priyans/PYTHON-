# 2.float() : To convert one possble value into float() value.
# Example1: int into float type--> Possible
a = 100
print(a,type(a)) # 100 <class 'int'>
b = float(a)
print(b,type(b)) # 100.0 <class 'float'>


# Example2: bool into float type--> Possible
a = True
print(a,type(a)) # True <class 'bool'>
b = float(a)
print(b,type(b)) # 1.0 <class 'float'> "Bcoz in this input 'True' PVM takes as 1"
c = False
print(c,type(c)) # False <class 'bool'>
d =float(c)
print(d,type(d)) # 0.0 <class 'float'> "Bcoz in this input 'False' PVM takes as 0"


# Example3: complex into float type--> Not Possible
# a = 7+23j
# print(a,type(a)) # (7+23j) <class 'complex'>
# b = float(a)
# print(b,type(b)) # TypeError: float() argument must be a string or a real number, not 'complex'

#This is not Included 
c = 6+9j
print(c,type(c))
print(c.real,type(c.real)) # 6.0 <class 'float'>
print(c.imag,type(c.imag)) # 9.0 <class 'float'>


# Example4: str into float type

#Case(a): str int into float type----> Possible
a = "100"
print(a,type(a)) # 100 <class 'str'>
b = float(a)
print(b,type(b)) # 100.0 <class 'float'>

#Case(b): str float into float type---->Possible
a = "45.56"
print(a,type(a)) # 45.56 <class 'str'>
b = float(a)
print(b,type(b)) # 45.56 <class 'float'>

#Case(c): str bool into float type----> Not Possible
# a = "True"
# print(a,type(a)) # True <class 'str'>
# b = float(a)
# print(b,type(b)) # ValueError: could not convert string to float: 'True' "Bcoz PVM taking as Pure string"

#Case(d): str complex into float type-----> Not Possible
# a = "45+897j"
# print(a,type(a)) # 45+897j <class 'str'>
# b = float(a)
# print(b,type(b)) # ValueError: could not convert string to float: '45+897j'

#Case(e): Pure str into float type----->
a = "PYTHON"
print(a,type(a)) # PYTHON <class 'str'>
b = float(a)
print(b,type(b)) # ValueError: could not convert string to float: 'PYTHON'


