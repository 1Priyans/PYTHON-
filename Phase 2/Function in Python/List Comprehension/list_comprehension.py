__Properties = '''
                    ==========================================================================
                                                List Comprehension 
                    ==========================================================================
 Syntax:
 ----------
                varname=[ Expression   for varname in IterableObject  if Test Cond  ]'''

# Write a python program for finding list of +ve and -ve separately by using List Comprehension
lst = [12, 13, 32, -23, -43, 24, 65, -65, 95]
pslist= [val for val in lst if val > 0]
nglist = [val for val in lst if val < 0]

print("Given List of values = {}".format(lst))
print("-"*80)
print("Positive List Values = {}".format(pslist))  # Positive List Values = [12, 13, 32, 24, 65, 95]
print("Negative List Values = {}".format(nglist))  # Negative List Values = [-23, -43, -65]
print("-"*80)


# Write a Python Program for for finding square for every element of given list.
lst = [12, 13, 32, -23, -43, 24, 65, -65, 95]
sqrlist = []
for val in lst:
    val = val**2
    sqrlist.append(val)
else:
    print("Given List: {}".format(lst))
    print("Square,Circle list: {}".format(sqrlist))  # Square,Circle list: [144, 169, 1024, 529, 1849, 576, 4225, 4225, 9025]


# Write a Python Program for for finding square for every element of given list by using List Comprehension.
lst = [12, 13, 32, -23, -43, 24, 65, -65, 95]
reslst = [val**2 for val in lst]  # List Comprehension
print("-"*80)
print("Given List = {}".format(lst))
print("-"*80)
print("Square,Circle List = {}".format(reslst), type(reslst))  # Square,Circle list: [144, 169, 1024, 529, 1849, 576, 4225, 4225, 9025] <class 'list'>



# Write a Python Program for for finding square for every element of given list by using List Comprehension.
lst = [12, 13, 32, -23, -43, 24, 65, -65, 95]
reslst = {val**2 for val in lst}  # # set Comprehension--> never maintains Order of Result--not recommended
print("-"*80)
print("Given List = {}".format(lst))
print("-"*80)
print("Square,Circle List = {}".format(reslst), type(reslst))  # Square,Circle List = {1024, 576, 4225, 9025, 169, 144, 529, 1849} <class 'set'> Bcoz set never maintains insertion order


# Write a Python Program for for finding square for every element of given list by using List Comprehension.
lst = [12, 13, 32, -23, -43, 24, 65, -65, 95]
reslst = (val**2 for val in lst)  # # set Comprehension--> never maintains Order of Result--not recommended
print("-"*80)
print("Given List = {}".format(lst))
print("-"*80)
print("Square,Circle List = {}".format(reslst), type(reslst))  # <generator object <genexpr> at 0x000000F0475222D0> <class 'generator'>
tpl = tuple(reslst)
print("Square,Circle List = {}".format(tpl), type(tpl))  # (144, 169, 1024, 529, 1849, 576, 4225, 4225, 9025) <class 'tuple'>



# Write a Python Program for for finding square for every element of given list by using List Comprehension.
lst = [12, 13, 32, -23, -43, 24, 65, -65, 95]
reslst = {(val, val**2) for val in lst}  # # set Comprehension--> never maintains Order of Result--not recommended
print("-"*80)
print("Given List = {}".format(lst))
print("-"*80)
print("Square,Circle List = {}".format(reslst), type(reslst))  # Square,Circle List = {(-23, 529), (32, 1024), (-43, 1849), (65, 4225), (24, 576), (12, 144), (95, 9025), (13, 169), (-65, 4225)} <class 'set'>


# Write a Python Program for for finding square for every element of given list by using List Comprehension.
lst = [12, 13, 32, -23, -43, 24, 65, -65, 95]
reslst = [(val, val**2) for val in lst]  # # set Comprehension--> never maintains Order of Result--not recommended
print("-"*80)
print("Given List = {}".format(lst))
print("-"*80)
dict = dict(reslst)
print("Square,Circle List = {}".format(dict), type(dict))  # Square,Circle List = {12: 144, 13: 169, 32: 1024, -23: 529, -43: 1849, 24: 576, 65: 4225, -65: 4225, 95: 9025} <class 'dict'>

# Write a Python Program for reading list of values dynaically from KBD by using List Comprehension
print("Enter the List of Values separated with spaces")
s = input()
print(s, type(s))
lst = s.split()
print(lst, type(lst)) # ['12', '23', '43', '34', '54', '56', '67', '877', '65', '54', '43', '23', '12'] <class 'list'>
for x in lst:
    print(x, type(x))

# OR
print("Enter the List of Values separated with spaces")
lst = [ int(x) for x in input().split()]
print(lst, type(lst))









