# map()
__Properties = '''map() is used for obtaining new Iterable object from existing iterable object by applying old iterable 
                  elements to the function.

In otherwords, map() is used for obtaining new list of elements  from  existing list of elements by applying old list elements 
to the function.

                Syntax:-      varname=map(FunctionName,Iterable_object)

Here 'varname' is an object of type <class,map'> and we can convert into any iteratable object by using type casting functions.

"FunctionName" represents either Normal function or anonymous functions.

"Iterable_object" represents Sequence, List, set and dict types.

The execution process of map() is that " map() sends every element of iterable object to the specified function, process 
it and returns the modified value (result) and new list of elements will be obtained". This process will be continued until 
all elements of Iterable_object completed.'''

# Example:
sqares = lambda n: n**2
# Main Program
print("Enter List of Numbers Separated by comma")
lst = list(int(val) for val in input().split())
finalsurlst = map(sqares, lst)
print("-"*70)
print("Type of finalsurlst = {}".format(type(finalsurlst)))  # <class 'map'>
print("Content of finalsurlst = {}".format(finalsurlst))  # <map object at 0x0000002A63887B20>
print("-"*70)
# To Convert class map to list() type we can use type casting functin
sqlist = list(finalsurlst)
print("Given List = {}".format(lst))  # Given List = [12, 21, 33, 44, 5, 6, 7, 8]
print("Square,Circle List = {}".format(sqlist)) # Square,Circle List = [144, 441, 1089, 1936, 25, 36, 49, 64]
print("-"*70)

# OR

sqares = lambda n: n**2
# Main Program
print("Enter List of Numbers Separated by comma")
lst = list(int(val) for val in input().split())
sqlist = list(map(sqares, lst))
print("-"*70)
print("Given List = {}".format(lst))  # Given List = [12, 21, 33, 44, 5, 6, 7, 8]
print("Square,Circle List = {}".format(sqlist)) # Square,Circle List = [144, 441, 1089, 1936, 25, 36, 49, 64]
print("-"*70)



# OR

print("Enter List of Numbers Separated by comma")
lst = list(int(val) for val in input().split())
sqlist = list(map(lambda n: n**2, lst))
print("-"*70)
print("Given List = {}".format(lst))  # Given List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Square,Circle List = {}".format(sqlist)) # Square,Circle List = [1, 4, 9, 16, 25, 36, 49, 64, 81, 0]
print("-"*70)

# Write a Python Program which will accept list of ild salary of employees dynamically and createting new salaries list.
print("Enter List of Old Salaries of Employee separated by comma:")
oldsallst = [int(val) for val in input().split(",") if int(val)>0 ]
newsallst = list(map(lambda sal: sal+sal*(50/100), oldsallst))
print("-"*70)
print("Old Salary of the Employees: {}".format(oldsallst))
print("New Salary of the Employees: {}".format(newsallst))
print("-"*70)

# Write a Python Program which will accept two list of dynamically and createting sum of two dynamically typed numerical new list.
print("Enter First List of  comma:")
lst1 = [int(val) for val in input().split(",") ]
print("Enter First List of  comma:")
lst2 = [int(val) for val in input().split(",") ]
# finding sum of elements of lst1 and lst2 in lst3=
lst3 = list(map(lambda a,b: a + b, lst1,lst2))
print("List1 = {}".format(lst1)) # List1 = [12, 21, 32, 13, 213, 321312, 1123, 2]
print("List2 = {}".format(lst2)) # List2 = [1232, 32, 123, 423, 543, 23]
print("List3 = {}".format(lst3)) # List3 = [1244, 53, 155, 436, 756, 321335]











