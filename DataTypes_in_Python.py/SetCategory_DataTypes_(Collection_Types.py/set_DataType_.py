__Properties = '''1) 'set' is a pre-defined class and treated as set data type.

2)The purpose of set data type is that "To Store Multiple Values either of Same Type or Different type or 
    Both the Types into single object with Unique Values (Duplicates are not allowed)".

3)The Elements / Data of set Must be Organized OR Stored within Curly Braces {} and the Values must 
     be  separted by comma.

4)An object of set never maintains Insertion Order bcoz set can display any Possibility of elements of 
    set (Set Elements are Un-ordered).

5)On the object of set , we can't perform Indexing and Slicing Operations bcoz set never maintains 
    Insertion Order.

6)An object of set belongs to Both Mutable  in the case of adding the elements and Immutable in the 
    case of Item Assignment.

7)We can create types of set objects. they  are
			1. empty set
			2. non-empty set
Empty list: 
            Syntax: setobj = set()
Non-Empty list:
            Syntax: setobj = {val1,val2,val3......val-n}
                    setobj = set(object)'''

#Example 
s1 = {10, 20, 30, "Mavrick", 5+3j}
print(s1,type(s1),id(s1)) # {20, 30, 10, 'Mavrick', (5+3j)} <class 'set'> 503085065920
print(s1[0]) # TypeError: 'set' object is not subscriptable
print(s1,type(s1),id(s1)) # {'Mavrick', 20, 30, 10, (5+3j)} <class 'set'> 503085065920

s2 = {"python", 1991, "Rossum", "jython", 3+6j}
print(s2,type(s2),id(s2)) # {'jython', 'python', (3+6j), 1991, 'Rossum'} <class 'set'> 582819572288
s2[0] = 10
print(s2,type(s2),id(s2)) # TypeError: 'set' object does not support item assignment
print(s2,type(s2),id(s2)) # {(3+6j), 'python', 1991, 'jython', 'Rossum'} <class 'set'> 582819572288
print(s2[::-1])  # TypeError: 'set' object is not subscriptable

st = {"python", 1991, "Rossum", "jython", 3+6j}
print(st,type(st),id(st)) # {'jython', 'python', (3+6j), 'Rossum', 1991} <class 'set'> 582819572288
st.add("TEX")
print(st,type(st),id(st)) # {'jython', 'TEX', 'python', (3+6j), 'Rossum', 1991} <class 'set'> 582819572288

st1 = set()
print(st1,type(st1),id(st1)) # set() <class 'set'> 582819572288
print(len(st1)) # 0

st1 = {}
print(st1,type(st1),id(st1)) # {} <class 'dict'> "Treated as dic data type not set"

s1 = [10, 20, 30, "Mavrick", 5+3j]
print(s1,type(s1),id(s1)) # [10, 20, 30, 'Mavrick', (5+3j)] <class 'list'> 682655586048
s2 = set(s1)
print(s2,type(s2),id(s2)) #  {'Mavrick', 10, (5+3j), 20, 30} <class 'set'> 682655868608





