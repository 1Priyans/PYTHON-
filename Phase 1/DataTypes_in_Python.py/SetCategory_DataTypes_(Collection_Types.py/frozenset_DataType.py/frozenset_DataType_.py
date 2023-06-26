_Properties = ''''1) frozenset' is one of the pre-defined class and treated as set data type.

2)The purpose of frozenset data type is that "To store Multiple Values either Simiar Type or Different 
  Type or Both the Types in Single Object with Unique  Values".

3)The elements of frozenset must be obtained from different objects like set , tuple and list.
		            Syntax:   frozensetobj=frozenset(set/list/tuple)

4)An Object of frozenset never maintains Insertion Order bcoz PVM can display any one of the  possibility 
  of elements of frozenset object never maintains Insertion Order.

6)An object of frozenset belongs to  Immutable bcoz frozenset' object does not support item  assignment 
  and  not possible to modify / Change / add.

7)we can create two types of frozenset objects. They are
			a) Empty frozenset
			b) Non-Empty  frozenset

a) Empty frozenset:
An Empty  frozenset is one, which does not contain any elements and whose length is 0
            Syntax:        frozensetobj=frozenset()

b) Non-Empty frozenset:
=>A Non-Empty frozenset is one, which  contains  elements and whose length is >0
            Syntax:         frozensetobj=frozenset( { val1, val2, ....val-n } )

            Syntax:         frozensetobj=frozenset( ( val1, val2, ....val-n ) )

            Syntax:         frozensetobj=frozenset( [ val1, val2, ....val-n ] ) '''

fs = {10, 20, 30, 20, 30, 40, 50}
print(fs,type(fs),id(fs)) # {50, 20, 40, 10, 30} <class 'set'> 967161996992
fs1 = frozenset(fs)
print(fs1,type(fs1),id(fs1)) # frozenset({50, 20, 40, 10, 30}) <class 'frozenset'> 967161995872

# fs1.add("HD")
# print(fs1,type(fs1),id(fs1)) # AttributeError: 'frozenset' object has no attribute 'add'

# print(fs1[0]) # TypeError: 'frozenset' object is not subscriptable

fs2 = frozenset()
print(fs2,type(fs2),id(fs2)) # frozenset() <class 'frozenset'> 570232334688
print(len(fs2)) # 0

fs = [10, 20, 30, 20, 30, 40, 50]
print(fs,type(fs),id(fs))  # [10, 20, 30, 20, 30, 40, 50] <class 'list'> 693321427456 
fs1 = frozenset(fs)
print(fs1,type(fs1),id(fs1)) # frozenset({40, 10, 50, 20, 30}) <class 'frozenset'> 693321656000

fs = (10, 20, 30, 20, 30, 40, 50)
print(fs,type(fs),id(fs)) # 10, 20, 30, 20, 30, 40, 50) <class 'tuple'> 520300376032
fs1 = frozenset(fs)
print(fs1,type(fs1),id(fs1)) # frozenset({40, 10, 50, 20, 30}) <class 'frozenset'> 520305238624





