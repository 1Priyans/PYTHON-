# a) set inside of another set: NOT POSSIBLE
s1 = {"Rossum", 12, 23, {20, 19, 17}, "Hyd", {100, 99, 98}, "Python"}
print(s1,type(s1)) # TypeError: unhashable type: 'set'


# b) set inside of another Tuple:  POSSIBLE
s2 = ("Rossum", 12, 23, {20, 19, 17}, "Hyd", {100, 99, 98}, "Python")
print(s2,type(s2)) # ('Rossum', 12, 23, {17, 19, 20}, 'Hyd', {98, 99, 100}, 'Python') <class 'tuple'>

for val in s2:
    print(val,type(val),type(s2))
# Rossum <class 'str'> <class 'tuple'>
# 12 <class 'int'> <class 'tuple'>
# 23 <class 'int'> <class 'tuple'>
# {17, 19, 20} <class 'set'> <class 'tuple'>
# Hyd <class 'str'> <class 'tuple'>
# {98, 99, 100} <class 'set'> <class 'tuple'>
# Python <class 'str'> <class 'tuple'>

s2[3].add(18)
print(s2,type(s2)) # ('Rossum', 12, 23, {17, 18, 19, 20}, 'Hyd', {98, 99, 100}, 'Python') <class 'tuple'>


# c) set inside of another List: POSSIBLE
s2 = ["Rossum", 12, 23, {20, 19, 17}, "Hyd", {100, 99, 98}, "Python"]
print(s2,type(s2)) # ['Rossum', 12, 23, {17, 19, 20}, 'Hyd', {98, 99, 100}, 'Python'] <class 'list'>

for val in s2:
    print(val,type(val),type(s2))
# Rossum <class 'str'> <class 'list'>
# 12 <class 'int'> <class 'list'>
# 23 <class 'int'> <class 'list'>
# {17, 19, 20} <class 'set'> <class 'list'>
# Hyd <class 'str'> <class 'list'>
# {98, 99, 100} <class 'set'> <class 'list'>
# Python <class 'str'> <class 'list'>

s2 = ["Rossum", 12, 23, {20, 19, 17}, "Hyd", {100, 99, 98}, "Python"]
s2[1].add(100)
print(s2,type(s2)) # AttributeError: 'int' object has no attribute 'add'

s2[3].add(100)
print(s2,type(s2)) # ['Rossum', 12, 23, {100, 17, 19, 20}, 'Hyd', {98, 99, 100}, 'Python'] <class 'list'>

s2[-2].add(100)
print(s2,type(s2)) # ['Rossum', 12, 23, {100, 17, 19, 20}, 'Hyd', {98, 99, 100}, 'Python'] <class 'list'>


#d) tuple inside of Another Set: POSSIBLE 
s2 ={"Rossum", 12, 23, (20, 19, 17), "Hyd", (100, 99, 98), "Python"}
print(s2,type(s2)) # {(100, 99, 98), 'Hyd', 23, 'Rossum', (20, 19, 17), 'Python', 12} <class 'set'>

for val in s2:
    print(val,type(val),type(s2))
# Python <class 'str'> <class 'set'>
# (100, 99, 98) <class 'tuple'> <class 'set'>
# 23 <class 'int'> <class 'set'>
# (20, 19, 17) <class 'tuple'> <class 'set'>
# Rossum <class 'str'> <class 'set'>
# 12 <class 'int'> <class 'set'>
# Hyd <class 'str'> <class 'set'>


#e) list inside of another set: NOT POSSIBLE
s2 ={"Rossum", 12, 23, [20, 19, 17], "Hyd", [100, 99, 98], "Python"}
print(s2,type(s2)) # TypeError: unhashable type: 'list'




