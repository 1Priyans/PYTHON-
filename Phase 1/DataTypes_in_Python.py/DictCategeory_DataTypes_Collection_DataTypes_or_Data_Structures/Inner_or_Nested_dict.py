# 1) Dict in Dict
d1={"sno":10,"sname":"RS","InternalMarks":{"CM":17,"C++":18,"PYTHON":17},"ExternalMarks":{"CM":77,"C++":66,"PYTHON":78},"Cname":"OUCET"}
print(d1,type(d1),id(d1))#{'sno': 10, 'sname': 'RS', 'InternalMarks': {'CM': 17, 'C++': 18, 'PYTHON': 17}, 'ExternalMarks': {'CM': 77, 'C++': 66, 'PYTHON': 78}, 'Cname': 'OUCET'} <class 'dict'> 558068120896

print(d1.get("ExternalMarks"),type(d1["ExternalMarks"])) # {'CM': 77, 'C++': 66, 'PYTHON': 78} <class 'dict'>
print(d1.get("sno"))

for a,b in d1.items():
    print((a,"------------->",b))
# This is the Output we got
#  ('sno', '------------->', 10)
# ('sname', '------------->', 'RS')
# ('InternalMarks', '------------->', {'CM': 17, 'C++': 18, 'PYTHON': 17})
# ('ExternalMarks', '------------->', {'CM': 77, 'C++': 66, 'PYTHON': 78})
# ('Cname', '------------->', 'OUCET')

for a in d1.get("ExternalMarks").keys():
    print(a)
# This is the Output we got
# CM
# C++
# PYTHON

for a in d1.get("ExternalMarks").items():
    print(a)
# This is the Output we got
# ('CM', 77)
# ('C++', 66)
# ('PYTHON', 78)

for a in d1.get("InternalMarks").items():
    print(a)
# This is the Output we got
# ('CM', 17)
# ('C++', 18)
# ('PYTHON', 17)

d1={"sno":10,"sname":"RS","InternalMarks":{"CM":17,"C++":18,"PYTHON":17},"ExternalMarks":{"CM":77,"C++":66,"PYTHON":78},"Cname":"OUCET"}
print(d1,type(d1),id(d1))#{'sno': 10, 'sname': 'RS', 'InternalMarks': {'CM': 17, 'C++': 18, 'PYTHON': 17}, 'ExternalMarks': {'CM': 77, 'C++': 66, 'PYTHON': 78}, 'Cname': 'OUCET'} <class 'dict'> 907448226496

d1["sno"] = 1000
print(d1,type(d1),id(d1))#{'sno': 1000, 'sname': 'RS', 'InternalMarks': {'CM': 17, 'C++': 18, 'PYTHON': 17}, 'ExternalMarks': {'CM': 77, 'C++': 66, 'PYTHON': 78}, 'Cname': 'OUCET'} <class 'dict'> 889180459712

print(d1.get("ExternalMarks").items()) # dict_items([('CM', 77), ('C++', 66), ('PYTHON', 78)])
for k,v in d1.get("ExternalMarks").items():
    print((k,v),type(d1))
# This is the Output we got
# ('CM', 77) <class 'dict'>
# ('C++', 66) <class 'dict'>
# ('PYTHON', 78) <class 'dict'>
 

#2)   list in dict
d1={"sno":10,"sname":"RS","crs1":["Python","Dsc","Django"],"crs2":["Java","C","C++"],"Cname":"OUCET"}
print(d1,type(d1),id(d1))#{'sno': 10, 'sname': 'RS', 'crs1': ['Python', 'Dsc', 'Django'], 'crs2': ['Java', 'C', 'C++'], 'Cname': 'OUCET'} <class 'dict'> 454807698752
for k,v in d1.items():
    print((k,'======>',v),type(d1))
# This is the Output we got
# ('sno', '======>', 10) <class 'dict'>
# ('sname', '======>', 'RS') <class 'dict'>
# ('crs1', '======>', ['Python', 'Dsc', 'Django']) <class 'dict'>
# ('crs2', '======>', ['Java', 'C', 'C++']) <class 'dict'>
# ('Cname', '======>', 'OUCET') <class 'dict'>

print(d1.get("crs1"),type(d1.get("crs1"))) # ['Python', 'Dsc', 'Django'] <class 'list'>


#3) tuple in dict
d1={"sno":10,"sname":"RS","crs1":("Python","Dsc","Django"),"crs2":("Java","C","C++"),"Cname":"OUCET"}
print(d1,type(d1),id(d1))#{'sno': 10, 'sname': 'RS', 'crs1': ('Python', 'Dsc', 'Django'), 'crs2': ('Java', 'C', 'C++'), 'Cname': 'OUCET'} <class 'dict'> 777138934464
for k,v in d1.items():
    print(k,'------------->',v)
# This is the Output we got
# sno -------------> 10
# sname -------------> RS
# crs1 -------------> ('Python', 'Dsc', 'Django')
# crs2 -------------> ('Java', 'C', 'C++')
# Cname -------------> OUCET


#4) set in dict
d1={"sno":10,"sname":"RS","crs1":{"Python","Dsc","Django"},"crs2":{"Java","C","C++"},"Cname":"OUCET"}
print(d1,type(d1),id(d1))#{'sno': 10, 'sname': 'RS', 'crs1': {'Django', 'Dsc', 'Python'}, 'crs2': {'C', 'C++', 'Java'}, 'Cname': 'OUCET'} <class 'dict'> 45652557120
for k,v in d1.items():
    print((k,'--------->',v))
# This is the Output we got
# ('sno', '--------->', 10)
# ('sname', '--------->', 'RS')
# ('crs1', '--------->', {'Django', 'Dsc', 'Python'})
# ('crs2', '--------->', {'C', 'C++', 'Java'})
# ('Cname', '--------->', 'OUCET')


#5) dict in list
l1=[10,"Rossum",{"CM":17,"Java":56},{"Python":56,"Dsc":34},"OUCET"]
print(l1,type(l1),id(l1)) # [10, 'Rossum', {'CM': 17, 'Java': 56}, {'Python': 56, 'Dsc': 34}, 'OUCET'] <class 'list'> 1094070204672
for val in l1:
    print(val,type(val),id(val),type(l1))
# This is the Output we got
# 10 <class 'int'> 219963982352 <class 'list'>
# Rossum <class 'str'> 219965654256 <class 'list'>
# {'CM': 17, 'Java': 56} <class 'dict'> 219965362880 <class 'list'>
# {'Python': 56, 'Dsc': 34} <class 'dict'> 219965275776 <class 'list'>
# OUCET <class 'str'> 219965600752 <class 'list'>


#6) dict in tuple
t1=(10,"Rossum",{"CM":17,"Java":56},{"Python":56,"Dsc":34},"OUCET")
print(t1,type(t1),id(t1))
for val in t1:
    print(val,type(val),type(t1))
# This is the Output we got
# 10 <class 'int'> <class 'tuple'>
# Rossum <class 'str'> <class 'tuple'>
# {'CM': 17, 'Java': 56} <class 'dict'> <class 'tuple'>
# {'Python': 56, 'Dsc': 34} <class 'dict'> <class 'tuple'>
# OUCET <class 'str'> <class 'tuple'>


#7)dict in set --> Not Possible
# s1={10,"Rossum",{"CM":17,"Java":56},{"Python":56,"Dsc":34},"OUCET"}
# print(s1,type(s1),id(s1))  #TypeError: unhashable type: 'dict'


# Special Points: Conversion from list of tuples into dict

l1=[(10,"Rossum"),(20,"Travis"),(30,"Kinney")]
print(l1,type(l1)) # [(10, 'Rossum'), (20, 'Travis'), (30, 'Kinney')] <class 'list'>

d1 = dict(l1)
print(d1,type(d1)) # {10: 'Rossum', 20: 'Travis', 30: 'Kinney'} <class 'dict'>





