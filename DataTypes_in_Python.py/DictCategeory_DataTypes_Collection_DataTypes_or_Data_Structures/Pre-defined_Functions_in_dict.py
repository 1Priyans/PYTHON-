#To Perform Various Operations on dict object, we have pre-defined Functions in dict object. They are

#1. clear()
_Properties = '''       Syntax:  dictobj.clear()

1) This Function is used for removing all the elements of dict object.

2) When we call this function upon empty dict object then we get None as Result.'''

#Example:
d1 = {100 : "PYTHON", 200 : "Jython", 300 : "Django"}
print(d1,type(d1),id(d1)) # {100: 'PYTHON', 200: 'Jython', 300: 'Django'} <class 'dict'> 780417744448
print(len(d1)) # 3
d1.clear()
print(d1,type(d1),id(d1)) # {} <class 'dict'> 780417744448
print(d1.clear()) # None
print(len(d1)) # 0


#2. pop()
_Properties = '''       Syntax:  dictobj.pop(Key)

1) This Function is used removing (Key,Value) from dict object

2) If the Value of Key does not exist then we get KeyError.'''

#Example:
d1 = {100 : "PYTHON", 200 : "Jython", 300 : "Django"}
print(d1,type(d1),id(d1)) # {100: 'PYTHON', 200: 'Jython', 300: 'Django'} <class 'dict'> 1082313129600
d1.pop(100)
print(d1,type(d1),id(d1)) # {200: 'Jython', 300: 'Django'} <class 'dict'> 1082313129600
d1.pop(200)
print(d1,type(d1),id(d1)) # {300: 'Django'} <class 'dict'> 1082313129600
d1.pop(300)
print(d1,type(d1),id(d1)) # {} <class 'dict'> 1082313129600
# d1.pop(100)
# print(d1,type(d1),id(d1)) # KeyError: 100


#3. popitem()
_Properties = '''       Syntax:  dictobj.popitem()

1) This Function is used removing last (Key,Value) from non-empty dict object.

2)When we call this function upon empty  object then we get KeyError as Result'''

#Example:
d1={10:2.3,20:3.4,30:4.5,40:2.3}
print(d1,type(d1),id(d1)) # {10: 2.3, 20: 3.4, 30: 4.5, 40: 2.3} <class 'dict'> 1018548895296

print(d1.popitem()) # (40, 2.3)
print(d1,type(d1),id(d1)) # {10: 2.3, 20: 3.4, 30: 4.5} <class 'dict'> 1018548895296

print(d1.popitem()) # (30, 4.5)
print(d1,type(d1),id(d1)) # {10: 2.3, 20: 3.4} <class 'dict'> 1018548895296

print(d1.popitem()) # (20, 3.4)
print(d1,type(d1),id(d1)) # {10: 2.3} <class 'dict'> 1018548895296

print(d1.popitem()) # (10, 2.3)
print(d1,type(d1),id(d1)) # {} <class 'dict'> 1018548895296

# print(d1.popitem())
# print(d1,type(d1),id(d1)) # KeyError: 'popitem(): dictionary is empty'


#4. copy()
_Properties = '''       Syntax:   dictobj2=dictobj1.copy()

1) This Function is used for copying the content of one dict object into another dict object.'''

#Example:
d1={100:2.3, 200:3.4, 30:4.5, 400:2.3}
print(d1,type(d1),id(d1)) # {100: 2.3, 200: 3.4, 30: 4.5, 400: 2.3} <class 'dict'> 720364158592
d2 = d1.copy()
print(d2,type(d2),id(d2)) # {100: 2.3, 200: 3.4, 30: 4.5, 400: 2.3} <class 'dict'> 720364158528

d1[100] = 29.43
d2[234] = 21.32

print(d1,type(d1),id(d1)) # {100: 29.43, 200: 3.4, 30: 4.5, 400: 2.3} <class 'dict'> 720364158528
print(d2,type(d2),id(d2)) # {100: 2.3, 200: 3.4, 30: 4.5, 400: 2.3, 234: 21.32} <class 'dict'> 654632599104


#5. get()
_Properties = '''       Syntax: varname = dictobj.get(Key)

1) This Function is used for obtaining the Value of Value by passing the Value of Key.

2) If the value of Key does not exist then we get None as a Result.
                                OR
                        Syntax: dictobj[Key] '''

#Example:
d1={100:2.3,20:3.4,500:4.5,400:2.3}
print(d1,type(d1),id(d1))
d2 = d1.get(100)
print(d2) # 2.3
d2 = d1.get(20)
print(d2) # 3.4
d2 = d1.get(500)
print(d2) # 4.5
d2 = d1.get(400)
print(d2) # 2.3 

d2 = d1.get(1000)
print(d2) # None
                                                #OR

d1={100:2.3,20:3.4,50:4.5,400:2.3}
print(d1,type(d1),id(d1))
print(d1[100]) # 2.3
print(d1[20]) # 3.4
print(d1[50]) # 4.5
print(d1[400]) # 2.3
# print(d1[1000]) # KeyError: 1000


#6. keys()
_Properties = '''       Syntax: dictobj.keys()
                                
                                (OR)
                        
                        Syntax: varname=dictobj.keys()

1) This function is used for obtaining Values of Key and stored in varname and It is an object of 
     <class,dict-keys> '''

#Example:
d1={100:2.3,20:3.4,500:4.5,400:2.3}
print(d1,type(d1),id(d1))
print(d1.keys(),type(d1.keys())) # dict_keys([100, 20, 500, 400]) <class 'dict_keys'> 325532939648

d2 = d1.keys()
print(d2,type(d2),id(d2)) # dict_keys([100, 20, 500, 400]) <class 'dict_keys'> 325533269968

for val in d1.keys():
    print(val,type(val),d1.get(val),type(d1.get(val)),type(d1))
#This is the output we got
# 100 <class 'int'> 2.3 <class 'float'> <class 'dict'>
# 20 <class 'int'> 3.4 <class 'float'> <class 'dict'>
# 500 <class 'int'> 4.5 <class 'float'> <class 'dict'>
# 400 <class 'int'> 2.3 <class 'float'> <class 'dict'>

for k in d1.keys():
    print(k,d1[k])
# 100 2.3
# 20 3.4
# 500 4.5
# 400 2.3


#7. values()
_Properties = '''       Syntax: dictobj.values()
                                
                                (OR)
                        
                        Syntax: varname=dictobj.values()

1) This function is used for obtaining Values of value and stored in varname and It is an object of 
     <class,dict-values> '''


#Example
d1={100:2.3,20:3.4,500:4.5,400:2.3} 
print(d1,type(d1),id(d1)) # 100: 2.3, 20: 3.4, 500: 4.5, 400: 2.3} <class 'dict'> 977403624704
print(d1.values()) # dict_values([2.3, 3.4, 4.5, 2.3])

d2 = d1.values()
print(d2,type(d2),id(d2)) # dict_values([2.3, 3.4, 4.5, 2.3]) <class 'dict_values'> 977404002208

for val in d1.values():
    print(val,type(val),d1.get(val),type(d1.get(val)),type(d1))
# This is the output we got
# 2.3 <class 'float'> None <class 'NoneType'> <class 'dict'>
# 3.4 <class 'float'> None <class 'NoneType'> <class 'dict'>
# 4.5 <class 'float'> None <class 'NoneType'> <class 'dict'>
# 2.3 <class 'float'> None <class 'NoneType'> <class 'dict'>


#8. items()
_Properties = '''       Syntax: dict.items()

                                OR
                        
                        Syntax: dictobj2 = dictobj1.items()

1) This Function is used for obtaining the Value of Value by passing the Value of Key.

2) If the value of Key does not exist then we get None as a Result.
                                OR
                        Syntax: dictobj[Key] '''

#Example:
d1={10:2.3,20:3.4,30:4.5,40:2.3}
print(d1.items()) # {10: 2.3, 20: 3.4, 30: 4.5, 40: 2.3} <class 'dict'> 934730101888

d2 = d1.items() # dict_items([(10, 2.3), (20, 3.4), (30, 4.5), (40, 2.3)])
print(d2,type(d2),id(d2)) # dict_items([(10, 2.3), (20, 3.4), (30, 4.5), (40, 2.3)]) <class 'dict_items'> 934730432464

for a in d1.items():
    print(a,type(a),type(d1.items()))
# This is the output we got
# (10, 2.3) <class 'tuple'> <class 'dict_items'>
# (20, 3.4) <class 'tuple'> <class 'dict_items'>
# (30, 4.5) <class 'tuple'> <class 'dict_items'>
# (40, 2.3) <class 'tuple'> <class 'dict_items'>


for key,val in d1.items():
    print(key,val)
# This is the output we got
# 10 2.3
# 20 3.4
# 30 4.5
# 40 2.3


#9. update()
_Properties = '''       Syntax: dictobj1.update(dictobj2)

1) This Function is used for updating the dictobj1 values with dict object2 values.'''

#Example:
# d1={10:2.3,20:3.4}
# d2={50:5.5,60:3.4}
# print(d1,type(d1),id(d1)) # {10: 2.3, 20: 3.4} <class 'dict'> 58589756672
# print(d2,type(d2),id(d2)) # {50: 5.5, 60: 3.4} <class 'dict'> 58589756736
# d1.update(d2)
# print(d1,type(d1),id(d1)) # {10: 2.3, 20: 3.4, 50: 5.5, 60: 3.4} <class 'dict'> 58589756672
# print(d2,type(d2),id(d2)) # {50: 5.5, 60: 3.4} <class 'dict'> 58589756736

d1={10:2.3,20:3.4}
d2={10:5.5,60:3.4}
print(d1,type(d1),id(d1)) # {10: 2.3, 20: 3.4} <class 'dict'> 526581218560
print(d2,type(d2),id(d2)) # {10: 5.5, 60: 3.4} <class 'dict'> 526581218624
d1.update(d2) 
print(d1,type(d1),id(d1)) # {10: 5.5, 20: 3.4, 60: 3.4} <class 'dict'> 526581218560
print(d2,type(d2),id(d2))  # {10: 5.5, 60: 3.4} <class 'dict'> 526581218624

d1={10:2.3,20:3.4}
d2={10:200.3,20:3.4000}
print(d1,type(d1),id(d1)) # {10: 2.3, 20: 3.4} <class 'dict'> 354600776832
print(d2,type(d2),id(d2)) # {10: 200.3, 20: 3.4} <class 'dict'> 354600729856
d2.update(d1) 
print(d1,type(d1),id(d1))  # {10: 2.3, 20: 3.4} <class 'dict'> 354600776832
print(d2,type(d2),id(d2)) # {10: 2.3, 20: 3.4} <class 'dict'> 354600729856

d2.update(d1) 
print(d1,type(d1),id(d1))  # {10: 2.3, 20: 3.4} <class 'dict'> 354600776832
print(d2,type(d2),id(d2))  # {10: 2.3, 20: 3.4} <class 'dict'> 354600729856
