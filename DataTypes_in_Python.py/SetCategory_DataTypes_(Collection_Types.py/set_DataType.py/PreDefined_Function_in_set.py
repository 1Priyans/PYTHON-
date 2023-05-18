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


#3. discard():
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

# If the Specified Value does not exist then we never get KeyError
s2.discard('Wild')
print(s2,type(s2),id(s2)) # {'Fog'} <class 'set'> 853369416032

s2.discard('Fog')
print(s2,type(s2),id(s2)) # set() <class 'set'> 853369416032


#4. pop():
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


#5. copy():
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
