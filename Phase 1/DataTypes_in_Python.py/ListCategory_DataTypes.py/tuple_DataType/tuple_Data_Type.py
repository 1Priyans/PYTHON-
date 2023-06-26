_Properties = '''
1) 'tuple' is one of the pre-defined class and treated as List data Type.

2) The purpose of tuple data type is that "To  store Multiple Values either of Same type or Different 
    Types or Both Types with Unique and Duplicates in single object (Constant Values)".

3) The elements of tuple must be stored or organized within braces ( ) and Elements separated 
    by comma.

4) An object of tuple maintains Insertion Order 

5) An object of tuple belongs to Immutable bcoz tuple' object does not support item assignment.

6) On the object of tuple, we can perform both Indexing and Slicing Operations.

7) In Python Programming, we have Two Types of tuple objects. They are
			1. empty tuple
			2. non-empty tuple
    
    Syntax: tplobj= ( Val1,Val2,......val-n )
					(OR)
	        tplobj=tuple(object)
					(OR)
			tplobj=val1,val2....val-n '''

#Example: 
tpl = (78, "Mavrick", 34.98, 4+3j)
print(tpl,type(tpl))
print(tpl[1]) # Mavrick
print(tpl[-1]) # (4+3j)
print(tpl[-10]) # IndexError: tuple index out of range
tpl[1] = "Mav"
print(tpl) # TypeError: 'tuple' object does not support item assignment

tpl1 = 78, "Mavrick", 34.98, 4+3j
print(tpl1,type(tpl1)) # (78, 'Mavrick', 34.98, (4+3j)) <class 'tuple'>
print(tpl1[1]) # Mavrick
print(tpl1[-1]) # (4+3j)
tpl2 = tuple()
print(tpl2,type(tpl2)) # () <class 'tuple'>
print(len(tpl2)) # 0


