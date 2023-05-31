# Membership Operators:

__Properties = '''1) The purpose of Membership Operators is that "To Check the Existence of Specified value in an Iterable Object".

2) An Iterable Object is one, which contains Two or More Number of Values.
Examples: Sequence Data Types(str,bytes,bytearray,range)
		      List data Types ( list, tuple)
		      Set Data Types (set,frozenset)
		      dict data type (dict)

3) Note that Fundamental and NoneType Data Types are not belongs to Iterable Object.

In Python Programming, we have 2 Types of Membership Operators. They are
			1. in
			2. not in

1. in:    
                    Syntax:      Value in IterableObject

1) If the "Value" Present in IterableObject then "in" operator Returns True.
2)If the "Value" not Present in IterableObject then "in" operator Returns False.

2.  not in
                    Syntax:      Value not in IterableObject
1) If the "Value" not  Present  in IterableObject then "not in" operator Returns True
2) If the "Value" Present  in IterableObject then "not in" operator Returns False. '''

# Exampel:

a = "RUSSOM"
# print(a, type(a))

print("R" in a)  # True

print("U" in a)  # True

print("SS" in a)  # True

print("O" in a)  # True

print("M" in a)  # True

print("R" not in a)  # True

print("U" not in a)  # True

print("SS" not in a)  # True

print("O" not in a)  # True

print("M" not in a)  # True

print("RUS" in a)  # True

print("" in a)  # True

print(" " in a)  # False

print("SSOM" in a)  # True

print("OM" in a)  # True

print("MOSSUR" in a)  # False

print("MOSSUR" in a[::-1])  # True

# ------------------------------------------------------------------------------------------------------------------------

s = "PYTHON"
print(s, type(s))  # PYTHON <class 'str'>

print("PYTH" in s)  # True

print("PYTH" not in s)  # False

print("THON" not in s)  # False

print("PTO" in s)  # False

print( "PTO" not in s)  # True

print("HON" not in s)  # False

print("PON" not in s)  # True

print("NOH" in s)  # False

print("NOH" not in s[::-1])  # False

print("PON" in s[::2])  # False

print("PTO" not in s[::2])  # False

print("PTO" not in s[::2][::-1])  # True

# ------------------------------------------------------------------------------------------------------------------------
lst = [10, "Rossum", 23.45, True, 2+3j]
print(lst, type(lst))

print("Rossum" in lst)  # True

print(False not in lst)  # True

print(True not in lst)  # False

print('Ross' in lst)  # False

print('Ross' not in lst)  # True

print('Ross' not in lst[1])  # False

print('Ross' in lst[1])  # True

print('Ross' not in lst[1][::-1])  # True

print('Ross'[::-1] not in lst[1][::]) # True
# ------------------------------------------------------------------------------------------------------------------------

lst = [10, "Rossum", 23.45, True, 2+3j]
print(lst, type(lst))  # [10, 'Rossum', 23.45, True, (2+3j)] <class 'list'>

print(lst[-1] in lst)  # True

# print(lst[-1] in lst[4])  # TypeError: argument of type 'complex' is not iterable

# print(lst[-1].real in lst[len(lst)-1])  # TypeError: argument of type 'complex' is not iterable
# -----------------------------------------------------------------------------------------------------------------------

lst = [10, "Rossum", 23.45, True, "2+3j"]
print(lst, type(lst))  # [10, 'Rossum', 23.45, True, '2+3j'] <class 'list'>

print(lst[-1] in lst[4])  # True

print(lst in lst)  # False

s = "PYTHON"
print(s in s)  # True
# -----------------------------------------------------------------------------------------------------------------------

d1 = {10: "Apple", 20:"Mango", 30:"Kiwi"}
print(d1, type(d1))  # {10: 'Apple', 20: 'Mango', 30: 'Kiwi'} <class 'dict'>

# print(d1 in d1)  # TypeError: unhashable type: 'dict'

print("Apple" in d1)

print((30, "Kiwi") in d1)

for x in d1:
    print(x, type(x), type(d1))
# This is the output we get
# 10 <class 'int'> <class 'dict'>
# 20 <class 'int'> <class 'dict'>
# 30 <class 'int'> <class 'dict'>


print("Apple" in d1.values())  # True

# print("Apple"[::-1] not in d1.values()[::-1])  # TypeError: 'dict_values' object is not subscriptable


