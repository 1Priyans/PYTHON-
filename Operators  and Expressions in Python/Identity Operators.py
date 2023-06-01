# Identity Operators
__Properties = ''' The purpose of Identity Operators is that "To Check the memory address of Objects".

In Python Programming , We have Two Types of Identity Operators. They are
			 1. is
			 2. is not
1. is 
________________________________________________________________________________________________________________________
                        Syntax:        Obj1 is Obj2
a) Here 'is' operator returns True provided Obj1 and Obj2 Memory Addresses are Same

b)Here 'is' operator returns False provided Obj1 and Obj2 Memory Addresses are Different

2. is not 
________________________________________________________________________________________________________________________
                        Syntax:        Obj1 is not Obj2

a)Here 'is not' operator returns True provided Obj1 and Obj2 Memory Addresses are Different

b)Here 'is not ' operator returns False provided Obj1 and Obj2 Memory Addresses are Same. '''

# Example:
a = None
b = None
print(a, id(a))  # None 140726817888248
print(b, id(b))  # None 140726817888248
print(a is b)  # True
print(a is not b)  # False
#_______________________________________________________________________________________________________________________

d1 = {10:"Apple", 20:"Mango", 30:"Kiwi"}
d2 = {10:"Apple", 20:"Mango", 30:"Kiwi"}
print(d1, id(d1))  # {10: 'Apple', 20: 'Mango', 30: 'Kiwi'} 1088978335936
print(d2, id(d2))  # {10: 'Apple', 20: 'Mango', 30: 'Kiwi'} 1088978336192
print(d1 is d2)  # False # When we taking any collection of values then its memory addresses are not same
print(d1 is not d2)  # True
#_______________________________________________________________________________________________________________________

s1 = {10, 20, 30, 40}
s2 = {10, 20, 30, 40}
print(s1, id(s1))  #  {40, 10, 20, 30} 1011356756768
print(s2, id(s2))  #  {40, 10, 20, 30} 1011356754976
print(s1 is s2)  # False
print(s1 is not s2)  # True
#_______________________________________________________________________________________________________________________

fs1 = frozenset({10, 20, 30, 40})
fs2 = frozenset({10, 20, 30, 40})
print(fs1, id(fs1))  # frozenset({40, 10, 20, 30}) 314410493632
print(fs2, id(fs2))  # frozenset({40, 10, 20, 30}) 314410494976
print(fs1 is fs2)  # False
print(fs1 is not fs2)  # True
#_______________________________________________________________________________________________________________________

l1 = [10, 20, 30, 40]
l2 = [10, 20, 30, 40]
print(l1, id(l1))  # [10, 20, 30, 40] 187708895552
print(l2, id(l2))  # [10, 20, 30, 40] 187708898304
print(l1 is l2)  # False
print(l1 is not l2)  # True
#_______________________________________________________________________________________________________________________

t1 = (10, 20, 30, 40)
t2 = (10, 20, 30, 40)
print(t1, id(t1))  # (10, 20, 30, 40) 144699661328
print(t1, id(t1))  # (10, 20, 30, 40) 144699661328
print(t1 is t2)  # True
print(t1 is not t2)  # False
#_______________________________________________________________________________________________________________________

s1 = "PYTHON"
s2 = "PYTHON"
print(s1, id(s1))  # PYTHON 144657511984
print(s2, id(s2))  # PYTHON 144657511984
print(s1 is s2)  # True
print(s1 is not s2)  # False

s1 = "PYTHON"
s2 = "PYTHOn"
print(s1, id(s1))  # PYTHON 774982235696
print(s2, id(s2))  # PYTHOn 774982236016
print(s1 is s2)  # False
print(s1 is not s2)  # True
#_______________________________________________________________________________________________________________________

b1 = bytes([10, 20, 30, 40])
b2 = bytes([10, 20, 30, 40])
print(b1, id(b1))  # b'\n\x14\x1e(' 99208150928
print(b2, id(b2))  # b'\n\x14\x1e(' 99208150880
print(b1 is b2)  # False
print(b1 is not b2)  # True
#_______________________________________________________________________________________________________________________

b1 = bytearray([10, 20, 30, 40])
b2 = bytearray([10, 20, 30, 40])
print(b1, id(b1))  # bytearray(b'\n\x14\x1e(') 1089260584048
print(b2, id(b2))  # bytearray(b'\n\x14\x1e(') 1089260584112
print(b1 is b2)  # False
print(b1 is not b2)  # True
#_______________________________________________________________________________________________________________________

r1 = range(10, 20)
r2 = range(10, 20)
print(r1, id(r1))  # range(10, 20) 26888339296
print(r2, id(r2))  # range(10, 20) 26888339344
print(r1 is r2)  # False
print(r1 is not r2)  # True
#_______________________________________________________________________________________________________________________

# Here complex number are made of Real and Imaginary part and obtaining as floating values and so hence they are not following certainty bcoz of this is
# They are not having same memory addresses
c1 = 2 + 3j
c2 = 2 + 3j
print(c1, id(c1))  # (2+3j) 2681934897040
print(c2, id(c2))  # (2+3j) 2681934900656
print(c1 is c2)  # False
print(c1 is not c2)  # True
#_______________________________________________________________________________________________________________________

a = True
b = False
print(a, id(a))  # True 140727193553768
print(b, id(b))  # False 140727193553800
print(a is b)  # False
print(a is not b)  # True

a = True
b = True
print(a, id(a))  # True 140721137699688
print(b, id(b))  # True 140721137699688
print(a is b)  # True
print(a is not b)  # False

a = False
b = True
print(a, id(a))  # False 140721135799176
print(b, id(b))  # True 140721135799144
print(a is b)  # False
print(a is not b)  # True
#_______________________________________________________________________________________________________________________

# they are not following certainty so They are not having same memory addresses
a = 12.34
b = 12.34
print(a, id(a))  # 12.34 81688184752
print(b, id(b))  # 12.34 81688185456
print(a is b)  # False
print(a is not b)  # True
#_______________________________________________________________________________________________________________________

# Here 0---256 values contains Same Address when we store same value in Different Objects Other than those Values They Contins Different Address
a = 400
b = 400
print(a, id(a))  # 400 81688189008
print(b, id(b))  # 400 81688189168
print(a is b)  # False
print(a is not b)  # True

a = 10
b = 10
print(a, id(a))  # 10 695457612304
print(b, id(b))  # 10 695457612304
print(a is b)  # True
print(a is not b)  # False

a = 0
b = 0
print(a, id(a))  # 0 313073860816
print(b, id(b))  # 0 313073860816
print(a is b)  # True
print(a is not b)  # False

a = 256
b = 256
print(a, id(a))  #  256 185099624656
print(b, id(b))  #  256 185099624656
print(a is b)  # True
print(a is not b)  # False

a = 257
b = 257
print(a, id(a))  # 257 81688189008
print(b, id(b))  # 257 81688189328
print(a is b)  # False
print(a is not b)  # True
#_______________________________________________________________________________________________________________________

# Here -1 to -5 values contains Same Address when we store same value in Different Objects Other than those Values They Contins Different Address

a = -1
b = -1
print(a, id(a))  # -1 898481127600
print(b, id(b))  # -1 898481127600
print(a is b)  # True
print(a is not b)  # FalSe


a = -5
b = -5
print(a, id(a))  # -5 936711749680
print(b, id(b))  # 5 936711749680
print(a is b)  # True
print(a is not b)  # False

a = -10
b = -10
print(a, id(a))  # -10 274895355024
print(b, id(b))  # -10 274896377776
print(a is b)  # False
print(a is not b)  # True
#_______________________________________________________________________________________________________________________

a, b = 300, 300  # Multi Line Assigment
print(a, id(a))  # 300 898482166576
print(b, id(b))  # 300 898482166576
print(a is b)  # True
print(a is not b)  # False

a, b = -10, -10  # Multi Line Assigment
print(a, id(a))  # -10 898482167376
print(b, id(b))  # -10 898482167376
print(a is b)  # True
print(a is not b)  # False

a, b = 1.2, 1.2  # Multi Line Assigment
print(a, id(a))  # 1.2 898482166736
print(b, id(b))  # 1.2 898482166736
print(a is b)  # True
print(a is not b)  # False
#_______________________________________________________________________________________________________________________

l1, l2 = [10, "RS", 23.45],[10, "RS", 23.45]
print(l1, id(l1))  # [10, 'RS', 23.45] 898482475840
print(l2, id(l2))  # [10, 'RS', 23.45] 898482475904
print(l1 is l2)  # False
print(l1 is not l2)  # True
#_______________________________________________________________________________________________________________________

a = 1000
b = a  # Deep Copy
print(a,id(a))  # 1000 898482167024
print(b,id(b))  # 1000 898482167024
print(a is b)  # True
print(a is not b)  # False

a = 1.2
b = a  # Deep Copy
print(a,id(a))  # 1.2 898482166736
print(b,id(b))  # 1.2 898482166736
print(a is b)  # True
print(a is not b)  # False

l1 = [10, "RS", 23.45]
l2 = l1  # Deep Copy
print(l1, id(l1))  # [10, 'RS', 23.45] 898482469824
print(l2, id(l2))  # [10, 'RS', 23.45] 898482469824
print(l1 is l2)  # True
print(l1 is not l2)  # False

l1 = [10, "RS", 23.45]
l2 = l1.copy()  # Shallow Copy
print(l1, id(l1))  # [10, 'RS', 23.45] 898482475904
print(l2, id(l2))  # [10, 'RS', 23.45] 898482475840
print(l1 is l2)  # False
print(l1 is not l2)  # True

