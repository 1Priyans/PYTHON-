# Filter()
__Properties = '''filter() is used for  "Filtering out some elements from list of elements by applying to function".

                Syntax:-        varname=filter(FunctionName, Iterable_object)

---------------------
Explanation:
---------------------
Here 'varname' is an object of type <class,'filter'> and we can convert into any iteratable object by using type casting 
functions.

"FunctionName" represents either Normal function or anonymous functions.

"Iterable_object" represents Sequence, List, set and dict types.

The execution process of filter() is that  " Each Value of Iterable object sends to Function Name. If the function return 
True then the element will be filtered. if the Function returns False then that element will be neglected/not filtered ". 
This process will be continued until all elements of Iterable object completed.'''

# EXAMPLE:
# Write a Python Program which will accept list of values from keyboard and find Even and Odd Numbers separately by using filter() function.
def even(n):
    if (n%2 == 0):
        return True
    else:
        return False
def odd(n):
    if (n%2 != 0):
        return True
    else:
        return False
# Main Program
lst = [12, 34, 54, 23, 11, 56, 76, 89]
evennum = filter(even, lst)
oddnum = filter(odd, lst)
print("-"*70)
print("Content of evennum = {}".format(evennum), type(evennum))  # Content of evennum = <filter object at 0x000000D23F407A60> <class 'filter'>
print("Content of oddnum = {}".format(oddnum), type(oddnum))  # Content of oddnum = <filter object at 0x000000D23F4079D0> <class 'filter'>
print("-"*70)
# To View the Content of evennum and oddnum we can use type castinf funtion
print("-"*70)
finalevennum = list(evennum)
print("Geting Even Numbers")
print("Even Numbers From the Given List{}= {}".format(lst, finalevennum)) # Even Numbers From the Given List[12, 34, 54, 23, 11, 56, 76, 89]= [12, 34, 54, 56, 76]
print("-"*70)
finaloddnum = list(oddnum)
print("Getting Odd Numbers")
print("Odd Numbers From the Given List{} = {}".format(lst, finaloddnum)) # Odd Numbers From the Given List[12, 34, 54, 23, 11, 56, 76, 89] = [23, 11, 89]
print("-"*70)

# OR


# Write a Python Program which will accept list of values from keyboard and find Even and Odd Numbers separately by using filter() function.
even  = lambda n: n%2 == 0
odd = lambda n: n%2 !=0
#Main Program
lst = [12, 34, 54, 23, 11, 56, 76, 89]
finalevennums = list(filter(even, lst))  # list() is type Casting Fumction to convert filter to list
finaloddnums = list(filter(odd, lst))  # # list() is type Casting Fumction to convert filter to list
print("-"*70)
print("Given Even Numbers")
print("Even Numbers from the List{} = {}".format(lst,finalevennums)) # Even Numbers from the List[12, 34, 54, 23, 11, 56, 76, 89] = [12, 34, 54, 56, 76]
print("Odd Numbers from the List{} = {}".format(lst, finaloddnums)) # Odd Numbers from the List[12, 34, 54, 23, 11, 56, 76, 89] = [23, 11, 89]
print("-"*70)


# OR


lst = [12, 11, 13, 34, 24, 55, 56, 76, 89, 80]
finalevennums = list(filter((lambda n: n%2 == 0), lst))
finaloddnums = list(filter((lambda n: n%2 != 0), lst))
print("-"*70)
print("Given Even Numbers")
print("Even Numbers from the List{} = {}".format(lst,finalevennums)) # Even Numbers from the List[12, 34, 54, 23, 11, 56, 76, 89] = [12, 34, 54, 56, 76]
print("-"*70)
print("Given Odd Numbers")
print("Odd Numbers from the List{} = {}".format(lst, finaloddnums)) # Odd Numbers from the List[12, 34, 54, 23, 11, 56, 76, 89] = [23, 11, 89]
print("-"*70)

# OR
#
lst = [12, 11, 13, 34, 24, 55, 56, 76, 89, 80]
print("-"*70)
print("Given Even Numbers")
print("Even Numbers from the List{} = {}".format(lst,list(filter((lambda n: n%2 == 0), lst)))) # Even Numbers from the List[12, 34, 54, 23, 11, 56, 76, 89] = [12, 34, 54, 56, 76]
print("-"*70)
print("Given Odd Numbers")
print("Odd Numbers from the List{} = {}".format(lst, list(filter((lambda n: n%2 != 0), lst)))) # Odd Numbers from the List[12, 34, 54, 23, 11, 56, 76, 89] = [23, 11, 89]
print("-"*70)

# Write a Python Program which will accept list of values Dynamically from keyboard and find Even and Odd Numbers separately by using filter() function.
print("Enter the List od Numerical Values Separated with Spaces: ")
lst = [int(val) for val in input().split()]
if (len(lst) == 0):
    print("List is empty and Can't find Even and Odd")
else:
    finalevennums = list(filter(lambda n: n%2 == 0, lst))
    finaloddnums = list(filter(lambda n: n%2 != 0, lst ))
    print("Given Even Numbers")
    print("Even Numbers from the List{} = {}".format(lst,finalevennums)) # Even Numbers from the List[12, 23, 43, 54, 65, 34, 32, 543, 65, 65, 34] = [12, 54, 34, 32, 34]
    print("-"*70)
    print("Given Odd Numbers")
    print("Odd Numbers from the List{} = {}".format(lst, finaloddnums)) #Odd Numbers from the List[12, 23, 43, 54, 65, 34, 32, 543, 65, 65, 34] = [23, 43, 65, 543, 65, 65]
    print("-"*70)














