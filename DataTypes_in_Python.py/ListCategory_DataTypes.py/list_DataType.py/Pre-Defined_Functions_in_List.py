# Along with Indexing and Slicing Operations, we can also Perform Various Operations by using 
#   Pre-defined Functions present in list object. They are

#1. append():

#Syntax:   listobj.append(Value)
#This Function is used for appending (Adding at end) Single Value to the list.
#Example:
lst = ["m24", 5.55, 3+3j]
print(lst,type(lst),id(lst)) # ['m24', 5.55, (3+3j)] <class 'list'> 694109705984
lst.append("MAVERICK")
lst.append("MAVERICK")
lst.append("MAVERICK")
lst.append("MAVERICK")
print(lst,type(lst),id(lst))#['m24', 5.55, (3+3j), 'MAVERICK', 'MAVERICK', 'MAVERICK', 'MAVERICK'] <class 'list'> 694109705984


#2. insert()

_Properties = '''     Syntax:-   listobj.insert(index,Value)
a) Here Index Represents Either +ve or -ve

b) Here Value can be One or More(list)

c) This Function is used for adding The value to the list at Specified Valid Index.

d) If the Index Value is not existing at +Ve Side then the value Inserted at END/Last

e) If the Index Value is not existing at -Ve Side then the value Inserted at BEGIN / First
'''
#Example
lst1 = [234, 45.34, "Vicecity", 3+7j]
print(lst1,type(lst1),id(lst1)) # [234, 45.34, 'Vicecity', (3+7j)] <class 'list'> 395986958848
lst1.insert(34,"HYD")
print(lst1,type(lst1),id(lst1)) # [234, 45.34, 'Vicecity', (3+7j), 'HYD'] <class 'list'> 395986958848
lst1.insert(-1,"Messi")
print(lst1,type(lst1),id(lst1)) # [234, 45.34, 'Vicecity', (3+7j), 'Messi', 'HYD'] <class 'list'> 395986958848
lst1.insert(-100,"Ronaldo")
print(lst1,type(lst1),id(lst1)) # ['Ronaldo', 234, 45.34, 'Vicecity', (3+7j), 'Messi', 'HYD'] <class 'list'> 


#3. clear()
_Properties = '''Syntax:    listobj.clear()

a) This Function is used for Removing all the Values from list object

b) When call this Function upon Empty List object then we never get any Result / None
'''
#Example: 
lst2 = [10,"Rossum",45.67,"Python"]
print(lst2,type(lst2),id(lst2)) # [10, 'Rossum', 45.67, 'Python'] <class 'list'> 223043529280
lst2.clear()
print(lst2,type(lst2),id(lst2)) # [] <class 'list'> 223043529280
print([].clear()) # None
print(list().clear()) # None
print(lst2.clear()) # None




