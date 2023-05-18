_Properties = '''We know that on the object of tuple we can perform Both Indexing and Slicing Operations.

Along with  these operations, we can also perform other operations by using the following 
    pre-defined  Functions.

		1)index()
		2)count() '''

#Example 
# tpl = ("North", 34.45, 3+4j, 'South')
# print(tpl.index("North")) # 0
# print(tpl.index(34.45)) # 1
# print(tpl.index(3+4j)) # 2
# print(tpl.index("South")) # 3

# print(tpl.count("Sk")) # 0
# print(tpl.count("North")) # 1

# # NOTE:-   By Using  del Operator we can't  delete values of tuple object By using Indexing and slicing 
# #          but we can delete entire object

# tpl1 = ("North", 34.45, 3+4j, 'South')
# print(tpl1,type(tpl1),id(tpl1))
# # del tpl[0]
# # print(tpl) # TypeError: 'tuple' object doesn't support item deletion

# del tpl1 # # Here we are removing complete object.
# print(tpl1) # NameError: name 'tpl1' is not defined.

# MOST IMP:
_Properties = '''sorted():  This Function is used for Sorting the data of immutable object tuple and gives 
                  the sorted data in the form of list.

                  Syntax: listobj=sorted(tuple object) '''

#Example:
t1= (23, 34, 45, 67, 89, 43, 21)
print(t1,type(t1)) # (23, 34, 45, 67, 89, 43, 21) <class 'tuple'>
# t1.sort()
# print(t1,type(t1)) # AttributeError: 'tuple' object has no attribute 'sort'
t = sorted(t1)
print(t,type(t)) # [21, 23, 34, 43, 45, 67, 89] <class 'list'>
print(t1,type(t1)) # (23, 34, 45, 67, 89, 43, 21) <class 'tuple'>
t1 = tuple(t) # Converted sorted list into tuple
print(t1,type(t1)) # (21, 23, 34, 43, 45, 67, 89) <class 'tuple'>
                       
                            #OR

t3 = (-23, 34, -45, 67, -89, -43, 21)
print(t3,type(t3)) # (-23, 34, -45, 67, -89, -43, 21) <class 'tuple'>
t4 = list(t3)
print(t4,type(t4)) # [-23, 34, -45, 67, -89, -43, 21] <class 'list'>
t4.sort() 
print(t4,type(t4)) # [-89, -45, -43, -23, 21, 34, 67] <class 'list'>
t3 = tuple(t4)
print(t3,type(t3)) # (-89, -45, -43, -23, 21, 34, 67) <class 'tuple'>
t3 = t3[::-1]
print(t3,type(t3)) # (67, 34, 21, -23, -43, -45, -89) <class 'tuple'>



