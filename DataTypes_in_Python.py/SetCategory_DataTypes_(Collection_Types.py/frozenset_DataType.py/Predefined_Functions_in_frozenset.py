_Properties = '''frozenset  contains the following Functions
			            a) copy()
			            b) isdisjoint()
			            c) issuperset()
			            d) issubset()
			            e) union()
			            f) intersection()
			            g) difference()
			            h) symmertic_difference()
frozenset  does not contain the following Functions
			            a) clear()
			            b) add()
			            c) remove()
			            d) discard()
			            e) pop()
			            f) update()
NOTE:
    In General, Immutable Object content is Not Possible to copy( in the case of tuple). Where as in 
the case of frozenset, we are able to copy its content to another frozenset object. Here Original 
frozenset object and copied frozenset object contains Same Address and Not at all possible to 
Modify / Change their content.'''

# a) copy()
_Properties = '''Syntax:   setobj2=setobj1.copy()

This Function is used for copying the content of one set object to another set object.'''

fs = frozenset({10, 10, 20, 30, 40, 50, 60})
print(fs,type(fs),id(fs)) # frozenset({50, 20, 40, 10, 60, 30}) <class 'frozenset'> 322349525344
fs1 = fs.copy()
print(fs1,type(fs1),id(fs1)) # frozenset({50, 20, 40, 10, 60, 30}) <class 'frozenset'> 322349525344


#b) isdisjoint()
_Properties = '''Syntax:  setobj1.isdisjoint(setobj2)

a) This Funtion returns True provided setobj1 and setobj2 are disjoint(There is no Common Element).

b) This Funtion returns False provided setobj1 and setobj2 are joint(There is a Common Element).'''

fs = frozenset({10, 10, 20, 30, 40, 50, 60})
fs1 = frozenset({10, 12, 13, 14, 20})
fs2 = frozenset({45, 13, 33, 31})
# print(fs.isdisjoint(fs1)) # False
# print(fs.isdisjoint(fs2)) # True
# print(fs1.isdisjoint(fs2)) # False


#c) issuperset()
_Properties = '''Syntax: setobj1.issuperset(setobj2)

a) This Function returns True provided setobj1 contains all the elements of setobj2.

b) This Function returns False provided setobj1 not containing all the elements of setobj2.'''

fs = frozenset({10, 10, 20, 30, 40})
fs1 = frozenset({10, 20, 30, 40, 12, 13, 14, 20})
fs2 = frozenset({45, 13, 33, 31})
# print(fs1.issuperset(fs)) # True
# print(fs.issuperset(fs1)) # False
# print(fs1.issuperset(fs2)) # False
# print(fs.issuperset(fs2)) # False


#d) issubset()
_Properties = '''Syntax: setobj1.issubset(setobj2)

a) This Function Returns True Provided all Elements of setobj1 are present in setobj2 .

b) This Function Returns False Provided all Elements of setobj1 are not present in setobj2.'''
fs = frozenset({10, 10, 20, 30, 40})
fs1 = frozenset({10, 20, 30, 40, 12, 13, 14, 20})
fs2 = frozenset({45, 13, 33, 31})
print(fs1.issubset(fs)) # False
print(fs.issubset(fs1)) # True
print(fs1.issubset(fs2)) # False
print(fs.issubset(fs2)) # False


#e) union()
_Properties = '''Syntax: setobj3 = setobj1.union(setobj2)

a) This Function is used for comibining all the  unique elements of setobj1 and setobj2 and result 
    places in setobj3.'''
fs = frozenset({10, 10, 20, 30, 40})
fs1 = frozenset({10, 20, 30, 40, 12, 13, 14, 20})
fs2 = frozenset({45, 13, 33, 31})
fs3 = fs1.union(fs) 
print(fs3,type(fs3),id(fs3)) # frozenset({40, 10, 12, 13, 14, 20, 30}) <class 'frozenset'> 662066722656
fs4 = fs2.union(fs)
print(fs4,type(fs4),id(fs4)) # frozenset({33, 40, 10, 45, 13, 20, 30, 31}) <class 'frozenset'> 204476410880


#f) intersection()
_Properties = '''Syntax: setobj3=setobj1.intersection(setobj2)

a) This Function is used for Obtaining Common elements from setobj1 and setobj2 and result 
    placed in setobj3.'''
fs = frozenset({10, 10, 20, 30, 40})
fs1 = frozenset({10, 20, 30, 40, 12, 13, 14, 20})
fs2 = frozenset({45, 13, 33, 31})
fs4 = fs1.intersection(fs)
print(fs4,type(fs4)) # frozenset({40, 10, 20, 30}) <class 'frozenset'>
fs5 = fs2.intersection(fs1)
print(fs5,type(fs5)) # frozenset({13}) <class 'frozenset'>


#g) difference()                     
_Properties = '''Syntax: setobj3=setobj1.difference(setobj2)

a) This Function removes the common  elements of setobj1 and setobj2 and takes remaining Elements 
    from setobj1 and Place the result in setobj3'''
fs = frozenset({10, 10, 20, 30, 40})
fs1 = frozenset({10, 20, 30, 40, 12, 13, 14, 20})
fs2 = frozenset({45, 13, 33, 31})
fs4 = fs1.difference(fs)
print(fs4,type(fs4)) # frozenset({12, 13, 14}) <class 'frozenset'>
fs5 = fs2.difference(fs1)
print(fs5,type(fs5)) # frozenset({33, 45, 31}) <class 'frozenset'>


#h) symmertic_difference()
_Properties = '''Syntax: setobj3=setobj1.symmetric_difference(setobj2)

a)This Function removes the common  elements of setobj1 and setobj2 and takes remaining Elements 
    from setobj1 and setobj2  and Place the result in setobj3

b)Mathamatically: setobj3=setob1.symmetric_difference(setobj2)--->s1.union(s2).difference(s1.intersection(s2))
'''
fs = frozenset({10, 10, 20, 30, 40})
fs1 = frozenset({10, 20, 30, 40, 12, 13, 14, 20})
fs2 = frozenset({45, 13, 33, 31})
fs4 = fs1.symmetric_difference(fs)
print(fs4,type(fs4)) # frozenset({12, 13, 14}) <class 'frozenset'>
fs5 = fs2.symmetric_difference(fs1)
print(fs5,type(fs5)) # frozenset({10, 12, 14, 20, 30, 31, 33, 40, 45}) <class 'frozenset'>




