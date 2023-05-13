# 1.bool() : To convert one possble value into bool() value.
# ALL NON-ZERO VALUES ARE CONSIDERED AS TRUE
# ALL ZERO VALUES ARE CONSIDERED AS FALSE

# Example1: int type into bool type--> Possible
a = 756
print(a,type(a)) # 756 <class 'int'>
b = bool(a)
print(b,type(b)) # True <class 'bool'> "True Bcoz nonzero value"
c = -456
print(c,type(c)) # -456 <class 'int'>
d = bool(c)
print(d,type(d)) # True <class 'bool'> "True Bcoz nonzero value"
e = 0
print(e,type(e)) # 0 <class 'int'>
f = bool(e)
print(f,type(f)) # False <class 'bool'> "False Bcoz zero value"
g = 309090
print(g,type(g)) # 309090 <class 'int'>
h = bool(g)
print(h,type(h)) # True <class 'bool'>


# Example2: float type into bool type-->Possible
a = 34.46
print(a,type(a)) # 34.46 <class 'float'>
b = bool(a)
print(b,type(b)) # True <class 'bool'> "True Bcoz nonzero value"
c = -43.567
print(c,type(c)) # -43.567 <class 'float'>
d = bool(c)
print(d,type(d)) # True <class 'bool'>  "True Bcoz nonzero value"
e = 0.00000000000000000000000001
print(e,type(e)) #1e-26 <class 'float'>
f = bool(e)
print(f,type(f)) #True <class 'bool'>  "True Bcoz nonzero value" **************


# Example3: complex type into bool type-->Possible
a = 78+4j
print(a,type(a)) # (78+4j) <class 'complex'>
b = bool(a)
print(b,type(b)) # True <class 'bool'> "True Bcoz nonzero value"
c = 0+0j
print(c,type(c)) # 0j <class 'complex'>
d = bool(c)
print(d,type(d)) # False <class 'bool'> "False Bcoz zero value"


# Example4: str type into bool type

#Case(a): str int into bool type---->Possible
a = "342253"
print(a,type(a)) # 342253 <class 'str'>
b = bool(a)
print(b,type(b)) # True <class 'bool'> "True Bcoz nonzero value"
c = "00"
print(c,type(c)) # 00 <class 'str'>
d = bool(c)
print(d,type(d)) # True <class 'bool'> "True Bcoz PVM takes '00' as length which is 2 so i.e. its none zero"

#Case(b): str float into bool type---->Possible
a = "23.342"
print(a,type(a)) # 23.342 <class 'str'>
b = bool(a)
print(b,type(b)) # True <class 'bool'> "True Bcoz nonzero value"
c = "0.00"
print(c,type(c)) # 0.00 <class 'str'>
d = bool(c)
print(d,type(d)) # True <class 'bool'> "True Bcoz PVM takes '0.00' as length which is 4 so i.e. its none zero"

#Case(c): str bool into bool type---->Possible
a = "True"
print(a,type(a)) # True <class 'str'>
b = bool(a)
print(b,type(b)) # True <class 'bool'> "True Bcoz PVM takes 'True' as length which is 4 so i.e. its none zero"
c = "False"
print(c,type(c)) # False <class 'str'>
d = bool(c)
print(d,type(d)) # True <class 'bool'> "True Bcoz PVM takes 'True' as length which is 4 so i.e. its none zero"
c = "False"

#Case(d): str complex into bool type---->Possible
a = "34+45j"
print(a,type(a)) # 34+45j <class 'str'>
b = bool(a)
print(b,type(b)) # True <class 'bool'> "True Bcoz PVM takes 'True' as length which is 4 so i.e. its none zero"
c = "0+0j"
print(c,type(c)) # 0+0j <class 'str'>
d = bool(c)
print(d,type(d)) # True <class 'bool'> "True Bcoz PVM takes 'True' as length which is 4 so i.e. its none zero"

#Case(e): Pure str into bool type---->Possible
a = "PYTHON"
print(a,type(a)) # PYTHON <class 'str'>
b = bool(a)
print(b,type(b)) # True <class 'bool'> "True Bcoz PVM takes 'True' as length which is 4 so i.e. its none zero"

#Some Special Cases:
a = "    "
print(a,type(a)) #      <class 'str'> "space"
b = bool(a)
print(b,type(b)) # True <class 'bool'> "True Bcoz PVM takes '    ' as length which is 4 so i.e. its none zero"

c= ""
print(c,type(c)) #  <class 'str'>
d =bool(c)
print(d,type(d)) # False <class 'bool'> "False Bcoz PVM takes '' as length which is 0 so i.e. its zero"
print(len(c)) # 0



