properties = '''1.) 'bytes' is one of the  pre-defined class and treated as Sequence Data Type.

2.)The purpose of bytes data type is that "To implement end-to-end encryption".

3.)To Implement end-to-end encryption, bytes data type stores the range of values from 0 to 256(i.e It 
    stores 0 to 255 only).

4.)bytes data type does not contain any symbolic notation for storing bytes data. But we can convert 
    Other Type of values into bytes type by using bytes()

5.)Syntax:    varname=bytes(object)	

6.)On the object of bytes, we can perform Indexing and Slicing Operations

7.)An object of bytes maintains INSERTION ORDER. which is nothing but whatever the order we insert, 
    in the  same order  data will be displayed.

8.)An object of bytes belongs to IMMUTABLE bcoz 'bytes' object does not support item assignment'''

#Example:

# lst = [10,20,40,50,256,60] 
# print(lst,type(lst)) # [10, 20, 40, 50, 256, 60] <class 'list'>
# lst = bytes(lst)
# print(lst,type(lst)) # ValueError: bytes must be in range(0, 256) "that means 0 - 255 only"

# lst1 = [10,-20,40,50,255,60]
# print(lst1,type(lst1)) # [10, -20, 40, 50, 255, 60] <class 'list'>
# lst1 = bytes(lst1)
# print(lst1,type(lst1)) # ValueError: bytes must be in range(0, 256) 

lst2 = [10,0,40,50,255]
print(lst2,type(lst2)) # [10, 0, 40, 50, 255] <class 'list'>
lst2 = bytes(lst2)
print(lst2,type(lst2)) # b'\n\x00(2\xff<' <class 'bytes'> "In this output  'b'\n\x00(2\xff<' this encryption format or human unreadable format"

for a in lst2: # Here, a is random variable and ':' is called Indentation symbol
    print(a)
# the output we get      
# 10
# 0
# 40
# 50
# 255
for b in lst2[::-1]:
    print(b)
# the output we get
# 255
# 50
# 40
# 0
# 10

for c in lst2[3:4]:
    print(c)
# the output we get
# 50

c[0] = 100
print(c) # TypeError: 'int' object does not support item assignment