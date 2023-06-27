# String Handling
__Properties = """On String Data, we can perform Indexing, Slicing Operations and with these operations, we can also 
                  perform different type of operations by using pre-defined functions present in str object.
-----------------------------------------
Pre-defined Functions in str object
-----------------------------------------
1.) capitalize()
2.) title()
3.) index() 
4.) upper()
5.) lower()
6.) isupper()
7.) islower()
8.) isalpha()
10.) isdigit()
11.) isalnum()
12.) isspace()
13.) split() and split("str")
14.) join()
15.) count()
16.) startswith()
17.) endswith() 
18.) swapcase()"""

_ = '''
1) capitalize()
--------------------------------------------------------------------------------------------------------------------------------
=>This Function is used for capitalizing the first letter First word of a given Sentence only.

=>Syntax:      strobj.capitalize()
				
				(OR)
			   
			   strobj=strobj.capitalize()'''
# Example:
# a = "python"
# b = a.capitalize()
# print(b, type(b)) # Python <class 'str'>
# print(a, type(a)) # python <class 'str'>
#
# s = "python is oop lang"
# t = s.capitalize()
# print(t, type(t))  # Python is oop lang <class 'str'>
# print(s, type(s))  # python is oop lang <class 'str'>


_ = """
2) title():
--------------------------------------------------------------------------------------------------------------------------------
=>This is used for obtaining Title Case of a Given Sentence  (OR) Making all words First 
    Letters are capital.

Syntax:          s.title()
			
			        (OR)
			    
			    s=s.title()"""
# Example:
# a = "python"
# b = a.title()
# print(b, type(b)) # Python <class 'str'>
# print(a, type(a)) # python <class 'str'>
#
# s = "python is oop lang"
# t = s.title()
# print(t, type(t))  # Python Is Oop Lang <class 'str'>
# print(s, type(s))  # python is oop lang <class 'str'>


_ = """
3) index()
--------------------------------------------------------------------------------------------------------------------------------
=>This Function obtains Index of the specified Value
=>If the specified value does not exist then we get ValueError

Syntax:        strobj.index(Value)

Syntax:	indexvalue=strobj.index(value)

enumerate() is one the general function, which is used for finding Index and Value of any 
       Iterable object."""
# Example:
# a = "python"
# b = a.index('p')
# print(b, type(b)) # 0 <class 'int'>
# b = a.index('y')
# print(b, type(b)) # 1 <class 'int'>
# b = a.index('t')
# print(b, type(b)) # 2 <class 'int'>
# b = a.index('h')
# print(b, type(b)) # 3 <class 'int'>
# b = a.index('o')
# print(b, type(b)) # 4 <class 'int'>
# b = a.index('n')
# print(b, type(b)) # 5 <class 'int'>
# b = a.index('P')
# print(b, type(b)) # ValueError: substring not found
#
# s = "python is oop lang"
# t = s.index('i')
# print(t, type(t))  # 7 <class 'int'>
# print(s, type(s))  # python is oop lang <class 'str'>

# s = "PYTHON"
# for kv,vv in enumerate(s):
#     print("Index: {}, Value: {}".format(kv,vv))
# This is the Output we get
# Index: 0, Value: P
# Index: 1, Value: Y
# Index: 2, Value: T
# Index: 3, Value: H
# Index: 4, Value: O
# Index: 5, Value: N

# s = "Python is OOp Lang"
# for kv,vv in enumerate(s):
#     print("Index: {}, Value: {}".format(kv,vv))
# This is the Output we get
# Index: 0, Value: P
# Index: 1, Value: Y
# Index: 2, Value: T
# Index: 3, Value: H
# Index: 4, Value: O
# Index: 5, Value: N
# Index: 0, Value: P
# Index: 1, Value: y
# Index: 2, Value: t
# Index: 3, Value: h
# Index: 4, Value: o
# Index: 5, Value: n
# Index: 6, Value:
# Index: 7, Value: i
# Index: 8, Value: s
# Index: 9, Value:
# Index: 10, Value: O
# Index: 11, Value: O
# Index: 12, Value: p
# Index: 13, Value:
# Index: 14, Value: L
# Index: 15, Value: a
# Index: 16, Value: n
# Index: 17, Value: g

# lst = ["Python", "Rossum", 1981, 1+23j]
# for kv,vv in enumerate(lst):
#     print("Index: {}, Value: {}".format(kv,vv)
# This is the Program we get
#     Index: 0, Value: Python
#     Index: 1, Value: Rossum
#     Index: 2, Value: 1981
#     Index: 3, Value: (1 + 23j)

_ = '''
4) upper()
--------------------------------------------------------------------------------------------------------------------------------
=>It is used for converting any type of Str Data into Upper Case.
=>Syntax:-   strobj.upper()
			
			      OR
			
			strobj=strobj.upper()'''
# Example:
# s = "Python"
# print(s, type(s))  # Python <class 'str'>
# t = s.upper()
# print(t,type(t))  # PYTHON <class 'str'>
# print(s,type(s))  # Python <class 'str'>
#
# s1 = "PyThon is OOp LanGuage"
# print(s1,type(s1))  # PyThon is OOp LanGuage <class 'str'>
# t1 = s1.upper()
# print(t1,type(t1))  # PYTHON IS OOP LANGUAGE <class 'str'>
# print(s1,type(s1))  # PyThon is OOp LanGuage <class 'str'>
#
# s2 = "123456"
# t2 = s2.upper()
# print(t2,type(t2))  # 123456 <class 'str'>
# print(s2,type(s2))  # 123456 <class 'str'>


_ = '''
5) lower()
--------------------------------------------------------------------------------------------------------------------------------
=>It is used for converting any type of Str Data into lower Case.

Syntax:-   strobj.lower()

			     OR

		   strobj=strobj.lower()'''
# # Example:
# s = "Python"
# print(s, type(s))  # Python <class 'str'>
# t = s.lower()
# print(t,type(t))  # python <class 'str'>
# print(s,type(s))  # Python <class 'str'>
#
# s1 = "PyThon is OOp LanGuage"
# print(s1,type(s1))  # PyThon is OOp LanGuage <class 'str'>
# t1 = s1.lower()
# print(t1,type(t1))  # python is oop language <class 'str'>
# print(s1,type(s1))  # PyThon is OOp LanGuage <class 'str'>
#
# s2 = "123456"
# t2 = s2.lower()
# print(t2,type(t2))  # 123456 <class 'str'>
# print(s2,type(s2))  # 123456 <class 'str'>


_ = '''
6) isupper()
--------------------------------------------------------------------------------------------------------------------------------
=>This Function returns True provided the given str object data is purely Upper Case otherwise it returns False.

Syntax:     strobj.isupper()'''

# s = "Python"
# t = s.isupper()
# print(t, type(t))  # False <class 'bool'>
# print(s, type(s))  # Python <class 'str'>

# s1 = "123"
# t1 = s1.isupper()
# print(t1,type(t1))  # False <class 'bool'>
# print(s1, type(s1))  # 123 <class 'str'>

# s = "%$#^&@"
# t = s.isupper()
# print(t, type(t))  # False <class 'bool'>
# print(s, type(s))  # %$#^&@ <class 'str'>


_ = '''
7) islower()
--------------------------------------------------------------------------------------------------------------------------------
=>This Function returns True provided the given str object data is purely lower Case otherwise it returns False.

	Syntax:     strobj.islower()'''
# # Example:
# s = "python"
# t = s.islower()
# print(t,type(t))  # True <class 'bool'>
# print(s,type(s))  # python <class 'str'>
#
# s1 = "PYTHON"
# t1 = s1.islower()
# print(t1,type(t1))  # False <class 'bool'>
# print(s1,type(s1))  # PYTHON <class 'str'>
#
# s2 = "PyThon"
# t2= s1.islower()
# print(t2,type(t2))  # False <class 'bool'>
# print(s2,type(s2))  # PyThon <class 'str'>
#
# s3 = '12345'
# t3 = s3.islower()
# print(t3, type(t3))  # False <class 'bool'>


_ = '''
8) isalpha()
--------------------------------------------------------------------------------------------------------------------------------
=>This Function returns True provided str object contains Purely Alphabets otherwise returns False.

		Syntax:   strobj.isalpha() '''
# # Example:
# s = "Ambition"
# t = s.isalpha()
# print(t,type(t))  # True <class 'bool'>
#
# s1 = "Ambition123241"
# t1 = s1.isalpha()
# print(t1,type(t1))  # False <class 'bool'>
#
# s2 = "AmBiTioN"
# t2 = s2.isalpha()
# print(t2,type(t2))  # True <class 'bool'>
#
# s3 = "Ambition123241"
# t3 = s3.isalpha()
# print(t3,type(t3))  # False <class 'bool'>
#
# s4 = "123241"
# t4 = s4.isalpha()
# print(t4,type(t4))  # False <class 'bool'>
#
# s5 = " "
# t5 = s5.isalpha()
# print(t5,type(t5))  # False <class 'bool'>


_ = '''
9) isdigit()
--------------------------------------------------------------------------------------------------------------------------------
=>This Function returns True provided given str object contains purely digits otherwise returns False'''
# # Example:
# s = "Ambition"
# t = s.isdigit()
# print(t,type(t))  # False <class 'bool'>
#
# s1 = "Ambition123241"
# t1 = s1.isdigit()
# print(t1,type(t1))  # False <class 'bool'>
#
# s2 = "12345"
# t2 = s2.isdigit()
# print(t2,type(t2))  # True <class 'bool'>
#
# s3 = "123241A"
# t3 = s3.isdigit()
# print(t3,type(t3))  # False <class 'bool'>
#
# s4 = "123 241"
# t4 = s4.isdigit()
# print(t4,type(t4))  # False <class 'bool'>
#
# s5 = " "
# t5 = s5.isdigit()
# print(t5,type(t5))  # False <class 'bool'>
#
# s6 = "12_34_56 "
# t6 = s6.isdigit()
# print(t6,type(t6))  # False <class 'bool'>

_ = '''
10) isalnum()
--------------------------------------------------------------------------------------------------------------------------------
=>This Function returns True provided str object contains either Alphabets OR Numerics or Alpha-Numerics only otherwise It returns False.

Syntax:   strobj. isalphanum()'''
# # Example:
# s = "Ambition"
# t = s.isalnum()
# print(t,type(t))  # True <class 'bool'>
#
# s1 = "Ambition123241"
# t1 = s1.isalnum()
# print(t1,type(t1))  # True <class 'bool'>
#
# s2 = "12345"
# t2 = s2.isdigit()
# print(t2,type(t2))  # True <class 'bool'>
#
# s3 = "@123241A"
# t3 = s3.isalnum()
# print(t3,type(t3))  # False <class 'bool'>
#
# s4 = "123 241"
# t4 = s4.isalnum()
# print(t4,type(t4))  # False <class 'bool'>
#
# s5 = " "
# t5 = s5.isalnum()
# print(t5,type(t5))  # False <class 'bool'>
#
# s6 = "12_A34_56 "
# t6 = s6.isalnum()
# print(t6,type(t6))  # False <class 'bool'>


_ = """
11) isspace()
-------------------------------------------------------------------------------------------------------------------------------
=>This Function returns True provided str obj contains purely space otherwise it returns False.

Syntax:    strobj.isspace()"""
# # Example
# s = ""
# t = s.isspace()
# print(t,type(t))  # False <class 'bool'>
#
# s1 = "  "
# t1 = s1.isspace()
# print(t1,type(t1))  # True <class 'bool'>
#
# s2 = "12345"
# t2 = s2.isspace()
# print(t2,type(t2))  # False <class 'bool'>
#
# s3 = "@12  3241A"
# t3 = s3.isspace()
# print(t3,type(t3))  # False <class 'bool'>
#
# s4 = " 1"
# t4 = s4.isspace()
# print(t4,type(t4))  # False <class 'bool'>


_ = """
12) split()
-------------------------------------------------------------------------------------------------------------------------------
This Function is used for splitting the given str object data into different words base specified delimter ( -  _  # % ^ ^ , ; ....etc)

The dafeult deleimter is space 

The Function returns Splitting data in the form of list object

Syntax:    strobj.split("Delimter")
				(OR)
			strobj.split()
				(OR)
			listobj=  strobj.split("Delimter")
				(OR)
			listobj=strobj.split()"""
# # Example:
# s = "Python is an OOp Language"
# print(len(s))  # 25
# t = s.split()
# print(t, type(t))  # ['Python', 'is', 'an', 'OOp', 'Language'] <class 'list'>
# print(len(t))  # 5
#
# s1 = "12-09-2022"
# t1 = s1.split()
# print(t1, type(t1))  # ['12-09-2022'] <class 'list'>
# t2 = s1.split("-")
# print(t2, type(t2))  # ['12', '09', '2022'] <class 'list'>
#
# s2 = "Apple#Banana#kiwi/Guava"
# t2 = s2.split()
# print(t2, type(t2))  # ['Apple#Banana#kiwi/Guava'] <class 'list'>
#
# t3 = s2.split("#")
# print(t3, type(t3))  # ['Apple', 'Banana', 'kiwi/Guava'] <class 'list'>
#
# t4 = s2.split("/")
# print(t4,type(t4))  # ['Apple#Banana#kiwi', 'Guava'] <class 'list'>


_ = """
13) join():
-------------------------------------------------------------------------------
=>This Function is used for combining or joining list of values from any Iterable object

Syntax:    strobj.join(Iterableobject)"""
# # Example:
# lst=["HYD","BANG","AP","DELHI"]
# print(lst,type(lst))
# lst1 = ""
# print(lst1.join(lst), type(lst1.join(lst)))  # HYDBANGAPDELHI <class 'str'>
#
# lst=["HYD","BANG","AP","DELHI"]
# print(lst,type(lst))
# lst2 = " "
# print(lst2.join(lst),type(lst1.join(lst2)))  # HYD BANG AP DELHI <class 'str'>
#
# list = ["Python", "is", "Dynamically", "Typed,", "Free & OpenSource", "and", "Robust", "Language"]
# print(list,type(list)) # ['Python', 'is', 'Dynamically', 'Typed', ',', 'Free & OpenSource', 'and', 'Robust', 'Language'] <class 'list'>
# list2 = " "
# print(list2.join(list),type(list2.join(list)))  # Python is Dynamically Typed, Free & OpenSource and Robust Language <class 'str'>


_ = """
14) count()
-----------
The count() fucntions returns the number of times a specified value appears in the string.

Syntax:   strobj.count(strvalue)"""
# # Example:
# s = "MISSISSIPPI"
# print(s.count("M")) # 1
# print(s.count("I")) # 4
# print(s.count("S")) # 4
# print(s.count("P")) # 2


_ = """
15) startswith()
---------------
Syntax:   strobj.startswith(strvalue)

The startswith()  returns True if the string starts with the specified value, otherwise False."""
# Example:
s = "python is an OOp lang"
print(s.startswith("python"))  # True
print(s.startswith("Python"))  # False
print(s.startswith("ython"))  # False


_ = """
16) endswith()
---------------
Syntax:   strobj.endswith(strvalue)

The functions  returns True if the string ends with the specified value, otherwise False."""
# Example
s = "python is an OOp lang"
print(s.endswith("lang"))  # True
print(s.endswith("Lang"))  # False
print(s.endswith("Python"))  # False





_ = """
17) swapcase()
--------------
The swapcase() functions returns a string where all the upper case letters are lower case and vice versa.

Syntax: strobj1.swapcase()"""
# # Example:
# s = "python"
# print(s.swapcase())  # PYTHON
#
# s1 = "PYTHON"
# print(s1.swapcase())  # python
#
# s2 = "PyThOn"
# print(s2.swapcase())  # pYtHoN
#
# s3 = "PYThon"
# print(s3.swapcase())  # pytHON
#
# s4 = "hyderabad"
# print(s4.swapcase())  # HYDERABAD
# print(s4.upper())
# print(s4.lower())







