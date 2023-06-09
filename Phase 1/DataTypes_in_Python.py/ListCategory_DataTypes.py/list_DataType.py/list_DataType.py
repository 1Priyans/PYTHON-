_Properties = '''1.)'list' is one of the pre-defined Class and treated as List Data Type.

2.)The purpose of list data type is that "To Store Multiple Values of Same Type or Different Type or Both 
    the types in single object with Unique and Duplicate.

3.)The Data in List object Stored / Organized within Square,Circle Brackets [ ] and They must be separated by 
    Comma.

4.)An object of list maintains Insertion Order.

5.)On the object of list, we can perform Both Indexing and Slicing Operations

6.)An an object of List belongs to Mutable bcoz Updation done at Same Address.

7.)In Python Programming, we have Two Types of List objects. They are
		a) Empty List
		b) Non-Empty List

a) Empty List

    An Empty List is one, which does not contain any Elements and whose Length is 0 
Syntax:         varname=[]
				(OR)
			varname=list()

b) Non-Empty List

    A Non-Empty List is one, which contains  Elements and whose Length is >0 
Syntax:         varname=[Val1,Val2....Val-n]
				(OR)
			varname=list(object)
'''

# Exaxmple
lst = [786, 80.52, "Soni", 4 + 34j]
print(lst, type(lst), id(lst))  # [786, 80.52, 'Soni', (4+34j)] <class 'list'> 404803696384
lst[0] = 100  # Updating Single value of List with Indexing
print(lst, type(lst), id(lst))  # [100, 80.52, 'Soni', (4+34j)] <class 'list'> 404803696384

lst[3:4] = ('Sk', 334)  # Updating Multiple value of List with Slicing
print(lst, type(lst), id(lst))  # [100, 80.52, 'Soni', 'Sk', 334] <class 'list'> 404803696384

print(lst[::-2])  # [334, 'Soni', 100]
print(lst[::-1])  # [334, 'Sk', 'Soni', 80.52, 100]

lst[:] = [786, 23.45, "Python", 4 + 43j]  # Replacing the list values
print(lst, type(lst), id(lst))  # [786, 23.45, 'Python', (4+43j)] <class 'list'> 404803696384

last1 = []  # To create Empty list
print(last1, type(last1), id(last1))  # [] <class 'list'> 404803696384

lst2 = list()
print(lst2, type(lst2), id(lst2))  # [] <class 'list'>  404803696384

lst3 = lst2[:] = [786, 23.45, "Python", 4 + 43j]
print(lst)  # [786, 23.45, 'Python', (4+43j)]
print(lst3)  # [786, 23.45, 'Python', (4+43j)]

lst4 = "PRIYANSH"
print(lst4, type(lst4), id(lst4))  # PRIYANSH <class 'str'> 963710661616
lst5 = list(lst4)
print(lst5, type(lst5), id(lst5))  # ['P', 'R', 'I', 'Y', 'A', 'N', 'S', 'H'] <class 'list'> 963710663360

lst6 = list([lst4])
print(lst6, type(lst6))  # ['PRIYANSH'] <class 'list'> "Special"
