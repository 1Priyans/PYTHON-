# Process of converting one possible value into another type of value is called Typecasting,
# We have 5 types of Fundamental casting techniques, They are
# 1. int(), 2. float(), 3. bool(), 4. complex(), 5. str()

# 1.int() : To convert one possble value into int() value.
# Example1: float type into int type-->Possible
a = 20.65
print(a,type(a)) # 20.65 <class 'float'>
b = int(a)
print(b,type(b)) # 20 <class 'int'> and its neglect the decimal places i.e. (.65)
c = 0.00
print(c,type(c)) # 0.0 <class 'float'>
d = int(c)
print(d,type(d)) # 0 <class 'int'>


#Example2: bool type into int-->Possible
a = True 
print(a,type(a)) # True <class 'bool'>
b = int(a)
print(b,type(b)) # 1 <class 'int'> Bcoz 'True' considered as 1
c = False
print(c,type(c)) # False <class 'bool'>
d = int(c)
print(d,type(d)) # 0 <class 'int'> Bcoz 'False' considered as 0


#Example3: complex type into int type-->Not Possible
a = 5+3j
print(a,type(a)) # (5+3j) <class 'complex'>
b = int(a)
print(b,type(b)) # TypeError: int() argument must be a string "bcoz PVM takes j as special symbol"

#This part is not included this is for Extra type casting Techniques
c = 6+7j
print(c.real,type(c.real)) # 6.0 <class 'float'>
d = int(c.real)
print(d,type(d)) # 6 <class 'int'>
print(c.imag,type(c.imag)) # 7.0 <class 'float'>
d = int(c.imag)
print(d,type(d)) # 7 <class 'int'>


#Example4: str type into int type

#Case(a): str int into int type----> Possible
a = "123"
print(a,type(a)) # 123 <class 'str'>
b = int(a)
print(b,type(b)) # 123 <class 'int'> "Bcoz PVM "123" takes as lengh  

#Case(b): str float into int type----> Not possible
a = "23.34"
print(a,type(a)) # 23.34 <class 'str'>
b = int(a)
print(b,type(b)) # ValueError: invalid literal for int() with base 10: '23.34' "Bcoz" In '23.34' PVM takes '.' point as special symbol 

#Case(c): str bool into int type----> Not possible
a = "True"
print(a,type(a)) # True <class 'str'>
b = int(a)
print(b,type(b)) # ValueError: invalid literal for int() with base 10: 'True' "bcoz" In 'True' PVM takes as ALPHABATES

#Case(d): str complex into int type---->Not Possible
a = "4+5j"
print(a,type(a)) # 4+5j <class 'str'>
b = int(a)
print(b,type(b)) # ValueError: invalid literal for int() with base 10: '4+5j'

#Case(e): Pure str into int type---->Not Possible
a = "PYTHON"
print(a,type(a)) # PYTHON <class 'str'>
b = int(a)
print(b,type(b)) # ValueError: invalid literal for int() with base 10: 'PYTHON'