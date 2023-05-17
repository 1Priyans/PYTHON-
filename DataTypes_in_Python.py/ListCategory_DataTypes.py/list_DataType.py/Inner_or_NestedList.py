_Properties = '''1) The Process of Defining one list inside of another list is called Inner or Nested List

        Syntax:- listobj=[ Val1, Val2....[Val11,Val12...Val1n], [Val21,Val22..Val2n...], Val-n ]

2) Here Val1,Val2...Val-n are called Values of Outer List

3) Here Val11,Val12...Val-1n are called Values of one Inner List

4) Here Val21,Val22...Val-2n are called Values of another Inner List

5) In inner list we can perform Both Indexing and Slicing Operations

6) On Inner List, we can apply all pre-defined function of list.'''

#Example:
lst = [100,"Mavrick",[19,18,16], [89,87,91], "Octopus"]
print(lst[2]) # [19, 18, 16]
print(lst[3]) # [89, 87, 91]
lst.append(23)
print(lst,type(lst)) # [100, 'Mavrick', [19, 18, 16], [89, 87, 91], 'Octopus', 23] <class 'list'>
lst[2].append(20)
print(lst,type(lst)) # [100, 'Mavrick', [19, 18, 16, 20], [89, 87, 91], 'Octopus', 23] <class 'list'>
lst[2].sort()
print(lst,type(lst)) # [100, 'Mavrick', [16, 18, 19, 20], [89, 87, 91], 'Octopus', 23] <class 'list'>
lst[3].sort()
print(lst,type(lst)) # [100, 'Mavrick', [16, 18, 19, 20], [87, 89, 91], 'Octopus', 23] <class 'list'>
lst[2].clear()
print(lst) # # [100, 'Mavrick', [], [87, 89, 91], 'Octopus', 23]
lst[3].clear() 
print(lst) #  [100, 'Mavrick', [], [], 'Octopus', 23]
del lst[2]
print(lst) # [100, 'Mavrick', [], 'Octopus', 23]
del lst[2]
print(lst) # [100, 'Mavrick', 'Octopus', 23]
lst.insert(-1,[19, 18, 16])
print(lst,type(lst)) # [100, 'Mavrick', 'Octopus', [19, 18, 16], 23] <class 'list'>
lst.insert(1,"Manic")
print(lst,type(lst)) # [100, 'Manic', 'Mavrick', 'Octopus', [19, 18, 16], 23] <class 'list'>

for val in lst:
    print(val,type(val),type(lst))
#This is the Output we get
# 100 <class 'int'> <class 'list'>
# Manic <class 'str'> <class 'list'>
# Mavrick <class 'str'> <class 'list'>
# Octopus <class 'str'> <class 'list'>
# [19, 18, 16] <class 'list'> <class 'list'>
# 23 <class 'int'> <class 'list'>

