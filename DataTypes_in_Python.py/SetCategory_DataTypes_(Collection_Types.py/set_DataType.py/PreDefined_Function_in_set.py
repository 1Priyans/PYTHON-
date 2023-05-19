# To perform Various Operations on set object, we use the following Pre-defined Functions which are 
#    present in set object.

#1. clear():
_Properties = '''Syntax:   setobj.clear()

1) This Function is used for removing all elements of set 
2) When we call this function upon empty set object then we get None.'''

#Example:
s1 = {10, 20, 30, "Mavrick", 5+3j}
print(s1,type(s1),id(s1)) # {'Mavrick', 20, 30, 10, (5+3j)} <class 'set'> 24483194560
s1.clear()
print(s1,type(s1),id(s1)) # set() <class 'set'> 24483194560
print(s1.clear()) # None


#2. add():
_Properties = '''Syntax:   setobj.add(value)

1) This Function is used for adding the values to the set object.'''

#Example
s1 = {10, 20, 30, "Mavrick", 5+3j}
print(s1,type(s1),id(s1)) # {'Mavrick', 20, 30, 10, (5+3j)} <class 'set'> 24483194560
s1.add("Hyd")
print(s1,type(s1),id(s1)) # {'Mavrick', 20, 30, 'Hyd', 10, (5+3j)} <class 'set'> 24483194560

s3 = set()
print(s3,type(s3),id(s3))  # set() <class 'set'> 908166883008
s3.add("Fog")
s3.add("Denver")
s3.add("Cobra")
s3.add("Wild Stone")
print(s3,type(s3),id(s3)) # {'Denver', 'Cobra', 'Wild Stone', 'Fog'} <class 'set'> 908166883008


#3. remove():
_Properties = '''Syntax: setobj.remove(value)

1) This Function is used for Removing the Specified Value from set object.
2) If the Specified Value does not exist then we get KeyError'''

#Example
s1 = {10, 20, 30, "Mavrick", 5+3j}
print(s1,type(s1),id(s1)) # {20, 'Mavrick', 30, 10, (5+3j)} <class 'set'> 656773212736
s1.remove(10)
print(s1,type(s1),id(s1)) # {20, 'Mavrick', 30, (5+3j)} <class 'set'> 656773212736
s1.remove(20)
print(s1,type(s1),id(s1)) # {'Mavrick', 30, (5+3j)} <class 'set'> 656773212736
s1.remove(30)
print(s1,type(s1),id(s1)) # {'Mavrick', (5+3j)} <class 'set'> 
s1.remove(5+3j)
print(s1,type(s1),id(s1)) # {'Mavrick'} <class 'set'> 340351379360
s1.remove("Mavrick")
print(s1,type(s1),id(s1)) # set() <class 'set'> 340351379360
s1.remove("Goku")
print(s1,type(s1),id(s1)) # KeyError: 'Goku' "Bcoz set contains unique values so that i.e. we get keyerror"


#4. discard():
_Properties = '''Syntax: setobj.discard(value)

1) This Function is used for Removing the Specified Value from set object.
2) If the Specified Value does not exist then we never get KeyError'''

#Example:
s2 = {'Denver', 'Cobra', 'Wild Stone', 'Fog'}
print(s2,type(s2),id(s2)) # {'Fog', 'Denver', 'Wild Stone', 'Cobra'} <class 'set'> 853369416032
s2.discard('Denver')
print(s2,type(s2),id(s2)) # {'Fog', 'Wild Stone', 'Cobra'} <class 'set'> 853369416032
s2.discard('Cobra')
print(s2,type(s2),id(s2)) # {'Fog', 'Wild Stone'} <class 'set'> 853369416032
s2.discard('Wild Stone')
print(s2,type(s2),id(s2)) # {'Fog'} <class 'set'> 853369416032

#If the Specified Value does not exist then we never get KeyError
s2.discard('Wild')
print(s2,type(s2),id(s2)) # {'Fog'} <class 'set'> 853369416032

s2.discard('Fog')
print(s2,type(s2),id(s2)) # set() <class 'set'> 853369416032


#5. pop():
_Properties = '''Syntax: setobj.pop()

1) This Function is used for removing any Arbitary Element from Non-Empty Set.
2) If the Specified Value does not exist then we get KeyError'''

#Example:
s2 = {'Denver', 'Cobra', 'Wild Stone', 'Fog'} # here There is no order of display i.e. remove arbitary Elements or random 
print(s2.pop()) # Denver
print(s2.pop()) # Fog
print(s2.pop()) # Wild Stone
print(s2.pop()) # Cobra
s2.pop()
print(s2,type(s2),id(s2)) # KeyError: 'pop from an empty set'
s2 = set()
print(s2,type(s2),id(s2)) # KeyError: 'pop from an empty set'

s2 = {'Denver', 'Cobra', 'Wild Stone', 'Fog'} # # Here we are showing Order of Display
print(s2,type(s2),id(s2)) # {'Cobra', 'Denver', 'Wild Stone', 'Fog'} <class 'set'> 222673693472
print(s2.pop()) # Cobra
print(s2.pop()) # Denver
print(s2.pop()) # Wild Stone
print(s2.pop()) # Fog
print(s2,type(s2),id(s2)) # set() <class 'set'> 222673693472

s3={10,20,30,40,50,60,70,80,90}
print(s3,type(s3),id(s3)) # {70, 40, 10, 80, 50, 20, 90, 60, 30} <class 'set'> 1033076731552
print(s3.pop()) # 70
print(s3.pop()) # 40
print(s3.pop()) # 10
print(s3.pop()) # 80
print(s3.pop()) # 50
print(s3.pop()) # 20
print(s3.pop()) # 90
print(s3.pop()) # 60
print(s3.pop()) # 30
print(s3,type(s3),id(s3)) # set() <class 'set'> 1033076731552


#6. copy():
_Properties = '''Syntax:   setobj2=setobj1.copy()
This Function is used for copying the content of one set object to another set object.'''

#Example 
s2 = {'Denver', 'Cobra', 'Wild Stone', 'Fog'}
s3 = s2.copy()
print(s3,type(s3),id(s3)) # {'Denver', 'Wild Stone', 'Cobra', 'Fog'} <class 'set'> 464362137952
print(s2,type(s2),id(s2)) # {'Denver', 'Wild Stone', 'Cobra', 'Fog'} <class 'set'> 464362138176

s2.add(100)
print(s2,type(s2),id(s2)) # {100, 'Fog', 'Cobra', 'Wild Stone', 'Denver'} <class 'set'> 363987135040
s3.add(200)
print(s3,type(s3),id(s3)) # {'Fog', 'Cobra', 200, 'Wild Stone', 'Denver'} <class 'set'> 363987134816

s2 = set()
s1 = s2.copy()
print(s1)  # set()
print(s2)  # set()
s2.clear()
print(s2) # set()


#7. isdisjoint():
_Properties = '''Syntax:  setobj1.isdisjoint(setobj2)

a) This Funtion returns True provided setobj1 and setobj2 are disjoint(There is no Common Element).

b) This Funtion returns False provided setobj1 and setobj2 are joint(There is a Common Element).'''

#Example
s1 = {10, 20, 30, 10, 70}
s2 = {20, 12, 55, 34}
s3 = {45, 13, 33, 31}
print(s1,type(s1)) # {10, 20, 70, 30} <class 'set'>
print(s2,type(s2)) # {34, 20, 12, 55} <class 'set'>
print(s3,type(s3)) # {33, 45, 13, 31} <class 'set'>
print(s1.isdisjoint(s2)) # False #There is a Common Element
print(s1.isdisjoint(s3)) # True  #There is no Common Element
print(s2.isdisjoint(s3)) # True # There is no Common Element


#8. isdisjoint():
_Properties = '''Syntax: setobj1.issubset(setobj2)

a) This Function Returns True Provided all Elements of setobj1 are present in setobj2 .

b) This Function Returns False Provided all Elements of setobj1 are not present in setobj2.'''

#Example
s1 = {10, 20}
s2 = {10, 20, 55, 30, 34}
s3 = {10, 13, 33, 31}
print(s1,type(s1)) # {20, 10} <class 'set'>
print(s2,type(s2)) # {34, 20, 12, 55} <class 'set'>
print(s3,type(s3)) # {33, 45, 13, 31} <class 'set'>

print(s1.issubset(s2)) # True  all Elements of setobj1 are present in setobj2
print(s2.issubset(s1)) # False  all Elements of setobj2 are not present in setobj1
print(s1.issubset(s3)) # False 
print(s2.issubset(s3)) # False


#9. issuperset():
_Properties = '''Syntax: setobj1.issuperset(setobj2)

a) This Function returns True provided setobj1 contains all the elements of setobj2.

b) This Function returns False provided setobj1 not containing all the elements of setobj2.'''

#Example:
s1 = {10, 20}
s2 = {10, 20, 55, 30, 34}
s3 = {10, 20, 13, 33, 31}
print(s2.issuperset(s1)) # True "Bcoz setobj2 contains all the elements of setobj1"
print(s1.issuperset(s2)) # False "setobj1 not containing all the elements of setobj2"
print(s3.issuperset(s1)) # True
print(s1.issuperset(s3)) # False 


#10. union():
_Properties = '''Syntax: setobj3 = setobj1.union(setobj2)

a) This Function is used for comibining all the  unique elements of setobj1 and setobj2 and result 
    places in setobj3.'''

#Example:
s1 = {10, 20}
s2 = {10, 20, 55, 30, 34}
s3 = {10, 20, 13, 33, 31}
s5 = s1.union(s2)
print(s5,type(s5)) # {34, 20, 55, 10, 30} <class 'set'>
s6 = s3.union(s1)
print(s6,type(s6)) # {33, 20, 10, 13, 31} <class 'set'>


#11. intersection():
_Properties = '''Syntax: setobj3=setobj1.intersection(setobj2)

a) This Function is used for Obtaining Common elements from setobj1 and setobj2 and result 
    placed in setobj3.'''

#Example:
s1 = {10, 20, 30}
s2 = {10, 20, 55, 30, 34}
s3 = {10, 20, 13, 33, 31}
s5 = s1.intersection(s2) 
print(s5,type(s5)) # {10, 20, 30} <class 'set'>
s6 = s3.intersection(s1) 
print(s6,type(s6)) # {10, 20} <class 'set'>

print({"Goku", "Suzume", "Naruto"}.intersection({10, 20, 30})) # set()


#12. difference():
_Properties = '''Syntax: setobj3=setobj1.difference(setobj2)

a) his Function removes the common  elements of setobj1 and setobj2 and takes remaining Elements 
    from setobj1 and Place the result in setobj3'''

#Example:
s1 = {10, 20, 30}
s2 = {10, 20, 55, 30, 34}
s3 = s1.difference(s2)
print(s3,type(s3)) # set() <class 'set'>

s4 = {10, 20, 44}
s5 = {10, 20, 55, 30, 34}
s6 = s4.difference(s5)
print(s6,type(s6)) # {44} <class 'set'>

s7 = {100, 200}.difference({10, 20})
print(s7,type(s7)) # {200, 100} <class 'set'>


#13. symmetric_difference():
_Properties = '''Syntax: setobj3=setobj1.symmetric_difference(setobj2)

a)This Function removes the common  elements of setobj1 and setobj2 and takes remaining Elements 
    from setobj1 and setobj2  and Place the result in setobj3

b)Mathamatically: setobj3=setob1.symmetric_difference(setobj2)--->s1.union(s2).difference(s1.intersection(s2))
'''

#Example:
s1 = {10, 20, 30}
s2 = {10, 20, 55, 30, 34}
s3 = s1.symmetric_difference(s2)
print(s3,type(s3)) # {34, 55} <class 'set'>

s4 = {10, 20, 30}
s5 = {10, 20, 30}
s6 = s4.symmetric_difference(s5)
print(s6,type(s6)) # set() <class 'set'>

s8 = {10, 100, 200, 300}.symmetric_difference({"HYD", 100, 200})
print(s8,type(s8)) # {10, 'HYD', 300} <class 'set'>


#14. update():
_Properties = '''Syntax: setobj1.update(setobj2)

a)This Function is used for comibining or mergining the  values of setobj1 and setbj2 in setobj1'''

#Example:
s1 = {"Tex", "Vandal", "Rabel", "Manic", "Bob"}
s2 = {"Tex", "Vandal", "Shawn", "Justin"}
s1.update(s2)
print(s1,type(s1)) # {'Bob', 'Justin', 'Rabel', 'Vandal', 'Shawn', 'Tex', 'Manic'} <class 'set'>
print(s2,type(s2)) # {'Shawn', 'Vandal', 'Tex', 'Justin'} <class 'set'>

s1 = {"Tex", "Vandal", "Rabel", "Manic", "Bob"}
s2 = {"Shawn", "Justin"}
s1.update(s2)
print(s1,type(s1)) # {'Justin', 'Rabel', 'Vandal', 'Manic', 'Bob', 'Tex', 'Shawn'} <class 'set'>
print(s2,type(s2)) # {'Justin', 'Shawn'} <class 'set'>

s1 = {"Tex", "Vandal"}
s2 = {"Tex", "Vandal"}
s1.update(s2)
print(s1,type(s1)) # {'Tex', 'Vandal'} <class 'set'>
print(s2,type(s2)) # 'Tex', 'Vandal'} <class 'set'>


_Properties = '''Consider the following statement
                    
                    python={"Rossum","Travis","Kinney"}
                    java={"Gosling","Ritche","Kerginan","Rossum"}

Find the following
a) all java and python learners.
b) Those ppl who learns both java and python
c) Those ppl who learns only python but not java
d) Those ppl who learns only java but not python
e) Those ppl who learns EXCLUSIVELY python and java.'''

#Solution:
Python={"Rossum","Travis","Kinney"}
Java={"Gosling","Ritche","Kerginan","Rossum"} 

allJaPy = Python.union(Java)
print(allJaPy,type(allJaPy)) #{'Gosling', 'Rossum', 'Travis', 'Kerginan', 'Kinney', 'Ritche'} <class 'set'>

bothJaPy = Python.intersection(Java)
print(bothJaPy,type(bothJaPy)) # {'Rossum'} <class 'set'>

onlyPy = Python.difference(Java)
print(onlyPy,type(onlyPy)) # {'Kinney', 'Travis'} <class 'set'>

onlyJa = Java.difference(Python)
print(onlyJa,type(onlyJa)) # {'Kerginan', 'Gosling', 'Ritche'} <class 'set'>

exclPyJa=Python.symmetric_difference(Java)
print(exclPyJa,type(exclPyJa)) # {'Kinney', 'Ritche', 'Gosling', 'Kerginan', 'Travis'} <class 'set'>


#And Without using set operation # Special Cases Examples with Bitwise Operator
Python={"Rossum","Travis","Kinney"}
Java={"Gosling","Ritche","Kerginan","Rossum"} 
 
allJaPy = Python | Java  # Bitwise OR
print(allJaPy,type(allJaPy)) # {'Rossum', 'Kinney', 'Ritche', 'Travis', 'Gosling', 'Kerginan'} <class 'set'>

bothJaPy = Python & Java # Bitwise AND
print(bothJaPy,type(bothJaPy)) # {'Rossum'} <class 'set'>

onlyPy = Python - Java  # Minus Operator
print(onlyPy,type(onlyPy)) # {'Travis', 'Kinney'} <class 'set'>

onlyJa = Java - Python
print(onlyJa,type(onlyJa)) # {'Gosling', 'Kerginan', 'Ritche'} <class 'set'>

exclPyJa= Python ^ Java # Bitwise XOR
print(exclPyJa,type(exclPyJa))

