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


# #2. insert()

# _Properties = '''     Syntax:-   listobj.insert(index,Value)
# a) Here Index Represents Either +ve or -ve

# b) Here Value can be One or More(list)

# c) This Function is used for adding The value to the list at Specified Valid Index.

# d) If the Index Value is not existing at +Ve Side then the value Inserted at END/Last

# e) If the Index Value is not existing at -Ve Side then the value Inserted at BEGIN / First
# '''
# #Example
lst1 = [234, 45.34, "Vicecity", 3+7j]
print(lst1,type(lst1),id(lst1)) # [234, 45.34, 'Vicecity', (3+7j)] <class 'list'> 395986958848
lst1.insert(34,"HYD")
print(lst1,type(lst1),id(lst1)) # [234, 45.34, 'Vicecity', (3+7j), 'HYD'] <class 'list'> 395986958848
lst1.insert(-1,"Messi")
print(lst1,type(lst1),id(lst1)) # [234, 45.34, 'Vicecity', (3+7j), 'Messi', 'HYD'] <class 'list'> 395986958848
lst1.insert(-100,"Ronaldo")
print(lst1,type(lst1),id(lst1)) # ['Ronaldo', 234, 45.34, 'Vicecity', (3+7j), 'Messi', 'HYD'] <class 'list'> 


# #3. clear()
# _Properties = '''Syntax:    listobj.clear()

# a) This Function is used for Removing all the Values from list object

# b) When call this Function upon Empty List object then we never get any Result / None'''

 #Example: 
lst2 = [10,"Rossum",45.67,"Python"]
print(lst2,type(lst2),id(lst2)) # [10, 'Rossum', 45.67, 'Python'] <class 'list'> 223043529280
lst2.clear()
print(lst2,type(lst2),id(lst2)) # [] <class 'list'> 223043529280
print([].clear()) # None
print(list().clear()) # None
print(lst2.clear()) # None


#4.remove()---> Based on Value
_Properties = ''' Syntax:-  listobj.remove(Value)

1) This Function  is used for Removing First Occurence of Specified Element.

2) If the Specified Elements does not exist then we get ValueError'''

#Example
list = ["Cube", 454, 90.34, 4+3j]
print(list,type(list),id(list)) # ['Cube', 454, 90.34, (4+3j)] <class 'list'> 1086150524224
print(list.remove("Cube"))
print(list,type(list),id(list)) # [454, 90.34, (4+3j)] <class 'list'> 1086150524224
print(list.remove(454))
print(list,type(list),id(list)) # [90.34, (4+3j)] <class 'list'> 1086150524224
print(list.remove(90.34))
print(list,type(list),id(list)) # [(4+3j)] <class 'list'> 1086150524224
print(list.remove(4+3j)) 
print(list,type(list),id(list)) # [] <class 'list'> 1086150524224
print(list.remove(4+3j)) 
print(list,type(list),id(list)) # ValueError: list.remove(x): x not in list

list2 = [10, 20, 10, 40, 10, 30, 40]
print(list2,type(list2),id(list2)) # [10, 20, 10, 40, 10, 30, 40] <class 'list'>  799654033152
print(list2.remove(10))
print(list2,type(list2),id(list2)) # [20, 10, 40, 10, 30, 40] <class 'list'>  799654033152 "Removing First Occurence of Specified Element"
print(list2.remove(10))
print(list2,type(list2),id(list2)) # [20, 40, 10, 30, 40] <class 'list'> 799654033152


#5. pop(Index)---> Index Based Removal
_Properties = '''Syntax:  listobj.pop(index)

1) This Function is used for Removing the Elemements of List based on Index.

2)If the Index is Invalid then we get IndexError.'''

list3 = [10, 20, 10, 40, 10, 30, 40]
print(list3,type(list3),id(list3)) # [10, 20, 10, 40, 10, 30, 40] <class 'list'> 880895211264
list3.pop(-1)
print(list3,type(list3),id(list3)) # [10, 20, 10, 40, 10, 30] <class 'list'> 880895211264
list3.pop(-30)
print(list3,type(list3),id(list3)) # IndexError: pop index out of range
print([].pop(10)) # IndexError: pop index out of range


#6. pop()
_Properties = ''' Syntax:listobj.pop()

1) This Function is used for Removing Last Element of non-list object.

2)If we call pop() upon empty list object then we get IndexError.'''

#Example:
list = ['Rossum', 1991, "PYTHON", 3+20j]
print(list,type(list),id(list)) # ['Rossum', 1991, 'PYTHON', (3+20j)] <class 'list'> 817088444160
print(list.pop()) # (3+20j)
print(list,type(list),id(list)) # ['Rossum', 1991, 'PYTHON'] <class 'list'> 817088444160
print(list.pop()) # PYTHON
print(list,type(list),id(list)) # ['Rossum', 1991] <class 'list'> 817088444160
print(list.pop()) # 1991 
print(list,type(list),id(list)) # ['Rossum'] <class 'list'> 817088444160
print(list.pop()) # Rossum
print(list,type(list),id(list)) # [] <class 'list'> 817088444160
print(list.pop()) 
print(list,type(list),id(list)) # IndexError: pop from empty list


#NOTE:  del Operator:
_Properties = '''Syntax-1:   del listobj[Index]----->Remove the element from list based on Index
		
Syntax-2:   del listobj[Begin:End:Step]--->Remove the element from list based on Slicing
		
Syntax-3:   del listobj---->Removes Total List object (Elements + object)'''

#Example:
list = ['Rossum', 1991, "PYTHON", 3+20j]
print(list,type(list),id(list)) # ['Rossum', 1991, 'PYTHON', (3+20j)] <class 'list'>  536742344448
del list[1]   # Based on Indexing
print(list,type(list),id(list)) # ['Rossum', 'PYTHON', (3+20j)] <class 'list'>  536742344448
del list[1:3] # Based on Slicing
print(list,type(list),id(list)) # ['Rossum'] <class 'list'>  536742344448

list6 = ['Rossum', 1991, "PYTHON", 3+20j]
print(list6) # ['Rossum', 1991, 'PYTHON', (3+20j)]
del list6
print(list6) # NameError: name 'list6' is not defined. Did you mean: 'list'?


#7. copy()
_Properties = ''' In Python Program, we have two types of Copy Techniques. They are
                  1)Shallow copy  2)Deep copy 

1)Shallow copy: a)This Function is used copying the content of one list object to another list object 
                  (Shallow Copy).
                
                b)Initial content of both the objects are same
                
                c)The memory address of both the objects are different
                
                d)Modification are independent (Whatever the changes we do on one object it won't 
                reflect to other object)
                
                d)To implement shallow copy we use copy()
                  Syntax: listobj2=listobj1.copy() '''

#Example
lt = ['Rossum', 1991, "PYTHON", 3+20j]
print(lt,type(lt),id(lt)) # ['Rossum', 1991, 'PYTHON', (3+20j)] <class 'list'> 844811024128
lt1 = lt.copy() 
print(lt1,type(lt1),id(lt1)) #['Rossum', 1991, 'PYTHON', (3+20j)] <class 'list'> 844811024125
print(lt,type(lt),id(lt)) #['Rossum', 1991, 'PYTHON', (3+20j)] <class 'list'> 8204891723482
print(lt.append("hyd")) 
print(lt,type(lt),id(lt)) # ['Rossum', 1991, 'PYTHON', (3+20j), 'hyd'] <class 'list'> 844811024128
print(lt1,type(lt1),id(lt1)) # ['Rossum', 1991, 'PYTHON', (3+20j)] <class 'list'> 844810975488
lt1 = lt.copy() 
print(lt,type(lt),id(lt)) # ['Rossum', 1991, 'PYTHON', (3+20j), 'hyd'] <class 'list'> 844811024128
print(lt1,type(lt1),id(lt1)) # ['Rossum', 1991, 'PYTHON', (3+20j), 'hyd'] <class 'list'> 844811020608

_Properties = '''

1)Deep copy: a)This Function is used copying the content of one list object to another list object 
                  (Deep Copy).
                
                b)Initial content of both the objects are same
                
                c)The memory address of both the objects are same
                
                d)Modification are dependent (Whatever the changes we do on one object it won't 
                reflect to other object)
                
                d)To implement Deep copy we use assignment operator(=)
                                Syntax: listobj2=listobj1   '''

#Example:
lst7 = ['Rossum', 1991, "PYTHON", 3+20j] 
print(lst7,type(lst7),id(lst7)) # ['Rossum', 1991, 'PYTHON', (3+20j)] <class 'list'> 202525914880
lst8 = lst7
print(lst8,type(lst8),id(lst8)) # ['Rossum', 1991, 'PYTHON', (3+20j)] <class 'list'> 202525914880
lst8.append("HYD")
print(lst7,type(lst7),id(lst7)) # ['Rossum', 1991, 'PYTHON', (3+20j), 'HYD'] <class 'list'> 202525914880
print(lst8,type(lst8),id(lst8)) # ['Rossum', 1991, 'PYTHON', (3+20j), 'HYD'] <class 'list'> 202525914880


#8. index()

_Properties = '''1) This Function is used  Finding Index of First occurence of Specified Element from non-empty list 
     object.

2) If the Specified Element does not exist then we get ValueError

3) If we call this function on empty-list object then we get ValueError
                
                Syntax:   listobj.index(Value)'''

#Example:
lst9 = ['Rossum', 1991, "PYTHON", 3+20j] 
print(lst9,type(lst9),id(lst9)) # ['Rossum', 1991, 'PYTHON', (3+20j)] <class 'list'> 848835458816
print(lst9.index('Rossum')) # 0
print(lst9.index(1991)) # 1
print(lst9.index("PYTHON")) # 2
print(lst9.index(3+20j)) # 3
print(lst9.index(10)) # ValueError: 10 is not in list
print(lst9.index(100)) # ValueError: 10 is not in list

# Enumerate Operater : 
lst10 = ['Rossum', 1991, "PYTHON", 3+20j]
print(lst10)
for ind,val in enumerate(lst10):
    print(ind,val)
#This is the ouput we get:
# 0 Rossum
# 1 1991
# 2 PYTHON
# 3 (3+20j)     


#9. count()
_Properties = '''1) This Function is used finding Number of Occurences of a specified Element.
                    
                    Syntax:  listobj.count(value)'''

#Example:
lst10 = ["Mav", "Rabel", "Vandal", "Tex", "Tex", "Mav", "Vandal", "Rabel", "Mav", "Mav", "Rabel"]
print(lst10,type(lst10),id(lst10))
print(lst10.count("Mav")) # 4
print(lst10.count("Rabel")) # 3
print(lst10.count("Vandal")) # 2
print(lst10.count("Tex")) # 2
print(lst10.count("HYD")) # 0
print(lst10.count(400)) # 0
print(lst10.count(4+67j)) # 0
print(list().count(100)) # 0
print([].count(0)) # 0

print(list("MAAAAAAIIIIIAAAIIISSSSIIISSTTTT").count("T")) # 4


#10. count()
_Properties = '''1)This Function is used for reversing (Front to back and Back to Front) the elements of 
                   List object.
                   
                   Syntax:   lstobj.reverse() '''

#Example:

lst10 = ['Rossum', 1991, "PYTHON", 3+20j] 
print(lst10,type(lst10),id(lst10)) # ['Rossum', 1991, 'PYTHON', (3+20j)] <class 'list'> 637010458368
lst11 = lst10.reverse()
print(lst10,id(lst10)) # [(3+20j), 'PYTHON', 1991, 'Rossum'] 637010458368
print(lst11,id(lst11)) # None 637010458368
lst11=lst10[::-1]
print(lst10,id(lst10))
print(lst11,id(lst11))


#11. sort()
_Properties = '''Syntax1:   listobj.sort()----->Used to Sort the data of list in Ascending Order
                
Syntax2:   listobj.sort(reverse=False)----->Used to Sort the data of list in Ascending Order

Syntax3:   listobj.sort(reverse=True)----------->Used to Sort the data of list in Decending Order '''

#Example:

lst = [10, 20, 10, -20, 55, 98, 234]
print(lst,type(lst),id(lst)) # [10, 20, 10, -20, 55, 98, 234] <class 'list'> 786989790976
lst.sort()  # Used to Sort the data of list in Ascending Order
print(lst,type(lst),id(lst)) # [-20, 10, 10, 20, 55, 98, 234] <class 'list'> 786989790976
lst.reverse() # another method used to sort the data in decending Order
print(lst,type(lst),id(lst)) # [234, 98, 55, 20, 10, 10, -20] <class 'list'> 786989790976

lst.sort(reverse= True)  # Used to Sort the data of list in Decending Order 
print(lst,type(lst),id(lst)) # [234, 98, 55, 20, 10, 10, -20] <class 'list'> 786989790976

lst.sort(reverse = False) # Used to Sort the data of list in Ascending Order
print(lst,type(lst),id(lst)) # [-20, 10, 10, 20, 55, 98, 234] <class 'list'> 786989790976

lsta = ["Mavrick", "Vandal", "Rebel", "Tex", "Razor", "Macnic"]
print(lsta,type(lsta),id(lsta)) # ['Mavrick', 'Vandal', 'Rebel', 'Tex', 'Razor', 'Macnic'] <class 'list'> 1087382255872
lsta.sort()
print(lsta,type(lsta),id(lsta)) # ['Macnic', 'Mavrick', 'Razor', 'Rebel', 'Tex', 'Vandal'] <class 'list'> 1087382255872

lstb = ["Mavrick", True, 29.12, 2332, "Razor", 3+4j]
print(lstb,type(lstb),id(lstb)) # ['Mavrick', True, 29.12, 2332, 'Razor', (3+4j)] <class 'list'> 15601510720
lstb.sort()
print(lstb,type(lstb),id(lstb)) # TypeError: '<' not supported between instances of 'bool' and 'str' 


#12. extend()
_Properties = '''Syntax: listobj1.extend(listobj2)

1)This Function is used for adding the content of listobj2 to listobj1

2)This Function can add only one list object content at a time to another list object but not multiple 
  list objects.

3)To extend multiple list objects at a time to list object, we use + operator

                Syntax: listobj1=listobj1+listobj2+....+listobj-n'''

#Example:
lst1 = [34, "HYD"]
lst2 = [423, "Python"]
lst1.extend(lst2)
print(lst1,type(lst1)) # [34, 'HYD', 423, 'Python'] <class 'list'>
lst2.extend(lst1)
print(lst2,type(lst2)) # [423, 'Python', 34, 'HYD', 423, 'Python'] <class 'list'>

#To Avoid this Problem, follow next Statements
lst1 = [34, "HYD"]
lst2 = [423, "Python"]
lst3 = [13, 43.32, "Soni"]
lst1.extend(lst2)
lst1.extend(lst2)
print(lst1,type(lst1)) # [34, 'HYD', 423, 'Python', 423, 'Python'] <class 'list'

# To extend multiple list objects at a time to list object, we use + operator
lst1 = [34, "HYD"]
lst2 = [423, "Python"]
lst3 = [13, 43.32, "Soni"]
lst1 = lst1 + lst2 + lst3 
print(lst1,type(lst1)) # [34, 'HYD', 423, 'Python', 13, 43.32, 'Soni'] <class 'list'> 






