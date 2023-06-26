__Properties = '''1)'dict' is one of the pre-defined class and treated as Dict Data Type.

2)The purpose of dict data type is that "To store (Key,value) in single variable"

3)In (Key,Value), the values of Key is Unique and Values of Value may or may not be unique.

4)The (Key,value) must be organized or stored in the object of dict within Curly Braces {} and  
  they separated by comma.

5)An object of dict does not support Indexing and Slicing bcoz Values of Key itself considered as Indices.

6)In the object of dict, Values of Key are treated as Immutable and Values of Value  are treated as mutable.

7)Originally an object of dict is mutable bcoz we can add (Key,Value) externally.

8)We have two types of dict objects. They are
			a) Empty dict
			b) Non-empty dict

a) Empty dict: Empty dict is one, which does not contain any (Key,Value) and whose length is 0
            
            Syntax:-          dictobj1= { }
				                   or
			                  dictobj=dict()
			    
            Syntax for adding (Key,Value) to empty dict:
                              
                              dictobj[Key1]=Val1
		                      dictobj[Key2]=Val2 

                              dictobj[Key-n]=Val-n
Here Key1,Key2...Key-n are called Values of Key and They must be Unique
Here Val1, Val2...Val-n are called Values of Value and They may or may not be unique.

b) Non-Empty dict: Non-Empty dict is one, which contains  (Key,Value) and whose length is >0

            Syntax:-       dictobj1= { Key1:Val1,Key2:Val2......Key-n:Valn}
			
Here Key1,Key2...Key-n are called Values of Key and They must be Unique
Here Val1, Val2...Val-n are called Values of Value and They may or may not be unique.'''

#Example:
d1 = {100 : "PYTHON", 200 : "Jython", 300 : "Django"}
print(d1,type(d1),id(d1)) # {100: 'PYTHON', 200: 'Jython', 300: 'Django'} <class 'dict'> 635179679296
d1[100] = "HYD"
d1[100] = "Karnataka"
d1[100] = "Banglore"
d1[100] = "Chennai"
d1[100] = "Pune"
print(d1,type(d1),id(d1)) # {100: 'Pune', 200: 'Jython', 300: 'Django'} <class 'dict'> 635179679296

d1[0] = "HYD"
print(d1,type(d1),id(d1)) # {100: 'Pune', 200: 'Jython', 300: 'Django', 0: 'HYD'} <class 'dict'> 635179679296

print(len(d1)) # 4

d2 = {}
print(d2,type(d2),id(d2)) # {} <class 'dict'> 729842433664
print(len(d2)) # 0
d2[200] = "CPyyhon"
print(d2,type(d2),id(d2)) # {200: 'CPyyhon'} <class 'dict'> 729842433664

d3 = dict()
print(d3,type(d3),id(d3)) # {} <class 'dict'> 1063436137920

d4 = dict()
d4["Python"]=1
d4["Java"]=3
d4["C"]=2
d4["GO"]=1
print(d4,type(d4),id(d4)) # {'Python': 1, 'Java': 3, 'C': 2, 'GO': 1} <class 'dict'> 772238980736
for val in d4:
    print(val,type(val),type(d4),id(d4))
# Python <class 'str'> <class 'dict'>  772238980736
# Java <class 'str'> <class 'dict'>  772238980736
# C <class 'str'> <class 'dict'> 772238980736
# GO <class 'str'> <class 'dict'>  772238980736

d5 = dict()
d5["Python"]=1
d5["Java"]=3
d5["C"]=2
d5["GO"]=1
d5[""] = 1
print(d5,type(d5),id(d5)) # {'Python': 1, 'Java': 3, 'C': 2, 'GO': 1, '': 1} <class 'dict'> 1006656796672
print(len(d5),type(d5),id(d5)) # 5 <class 'dict'> 1006656796672



