# 3. reduce()
import functools

__Properties = '''reduce() is used for obtaining a single element / result from given iterable object by applying to a function.

Syntax:-
		varname=reduce(function-name,iterable-object)

here varname is an object of int, float,bool,complex,str only
The reduce() belongs to a pre-defined module called" functools".

---------------------------------------
Internal Flow of reduce()
---------------------------------------
step-1:- Initially, reduce() selects  First Two values of Iterable object and place them in First var and Second var .

step-2:- The function-name(lambda or normal function) utilizes the values of First var and Second var and applied to 
         the specified logic and obtains the result.

Step-3:- reduce () places the result of function-name in First variable and reduce() selects the succeeding element of 
         Iterable object and places in second variable.

Step-4: Repeat  Step-2 and Step-3 until all elements completed in Iterable object and returns the result of First Variable.'''

#Example:
# # Write a python program which will finding sum of List of numbers by using reduce()
# import functools
# def addition(x, y):
#     z = x + y
#     return z
# #Main Program
# print("Enter List of Numbers Seperated by Space:")
# lst = [int(val) for val in input().split()]
# sumoflst = functools.reduce(addition, lst)
# print("-"*70)
# print("Sum of Numbers of Given List{} = {}".format(lst, sumoflst))
# print("-"*70)


# # Write a python program which will finding sum of List of numbers by using reduce() and Anonymous function
# print("Enter List of Numbers Seperated by Space:")
# lst = [int(val) for val in input().split()]
# sumoflst = functools.reduce(lambda a,b:a + b, lst)
# print("-"*70)
# print("Sum of Numbers of Given List{} = {}".format(lst, sumoflst))
# print("-"*70)


# #Write a Python Program for obtaining Max  and Min Element from List of Values by using reduce()
# print("Enter List of Numbers Seperated by Space:")
# lst = [int(val) for val in input().split()]
# maxvalue = functools.reduce(lambda a,b:a if a > b else b, lst)
# print("-"*70)
# print("Maximum Value of Given List{} = {}".format(lst, maxvalue))
# print("-"*70)
# minvalue = functools.reduce(lambda a,b:a if a < b else b, lst)
# print("Minimum Value of Given List{} = {}".format(lst, minvalue))
# print("-"*70)


#Write a Python Program for reading Multiple words and obtain a line of text by using reduce()
# print("Enter List of Words Seperated by Comma:")
# lst = [val for val in input().split(",")]
# wordsline = functools.reduce(lambda x,y: x+" "+y, lst) # Python,is,simple,&,opensource,interpreted,highlevel,dynamically,typed,lang.
# print("-"*70)
# print("Given list of word = {}".format(lst)) # Given list of word = ['Python', 'is', 'simple', '&', 'opensource', 'interpreted', 'highlevel', 'dynamically', 'typed', 'lang.']
# print("-"*70)
# print("Given Text Line: {}".format(wordsline)) # Given Text Line: Python is simple & opensource interpreted highlevel dynamically typed lang.
# print("-"*70)


# Program for obtaning Sum of +Ve and -Ve and from List of Numerical values by using filter() and reduce()
import functools
print("Enter List of Numbers separated by Space:")
lst = list((int(val) for val in input().split()))
print("-"*60)
print("Given List = {}".format(lst)) # Given List = [12, 32, 432, -234, -2432, 123, -231, -1, 3]
print("-"*60)
poslist = list(filter(lambda a: a > 0, lst))
poslstsum = functools.reduce(lambda a,b: a + b, poslist)
print("-"*60)
print("Positive List = {}".format(poslist))  # Positive List = [12, 32, 432, 123, 3]
print("Sum of Positive Numbers List  = {}".format(poslstsum))  # Sum of Positive Numbers List  = 602
print("-"*60)
neglist = list(filter(lambda a: a < 0, lst))
neglstsum = functools.reduce(lambda a,b: a - b, neglist)
print("-"*60)
print("Negative List = {}".format(neglist))  # Negative List = [-234, -2432, -231, -1]
print("Sum of Negative Numbers List  = {}".format(neglstsum))  # Sum of Negative Numbers List  = 2430
print("-"*60)