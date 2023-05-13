_Properties = '''1.)'bytearray' is one of the  pre-defined class and treated as Sequence Data Type.

2.)The purpose of bytearray data type is that "To implement end-to-end encryption".

3.)To Implement end-to-end encryption, bytearray data type stores the range of values from 0 to 256(i.e It 
    stores 0 to 255 only).

4.)bytearray data type does not contain any symbolic notation for storing bytearray data. But we can 
convert  Other Type of values into bytearray type by using bytearray()
    Syntax:    varname=bytearray(object)	

5.)On the object of bytearray, we can perform Indexing and Slicing Operations

6.)An object of bytearray maintains INSERTION ORDER. which is nothing but whatever the order we insert,  
    in the  same order  data will be displayed.

7.)An object of bytearray belongs to MUTABLE bcoz 'bytearray' object  support item assignment

NOTE: The Functionality of bytearray is extactly similar to bytes But an object of bytearray belongs to 
            MUTABLE where an object bytes belongs to IMMUTABLE.'''

#Example:

# lst = [10, 20, 30, 50, 270, 60]
# print(lst,type(lst)) # [10, 20, 30, 50, 270, 60] <class 'list'>
# lst = bytearray(lst)
# print(lst) # ValueError: byte must be in range(0, 256)

# lst = [-10, 20, 30, 50, 27, 60]
# print(lst,type(lst)) # [-10, 20, 30, 50, 27, 60] <class 'list'>
# lst = bytearray(lst)
# print(lst) # ValueError: byte must be in range(0, 256)

lst = [10, 20, 30, 50, 27, 60]
print(lst,type(lst)) # [10, 20, 30, 50, 27, 60] <class 'list'>
lst = bytearray(lst)
print(lst,type(lst),id(lst))  # bytearray(b'\n\x14\x1e2\x1b<') <class 'bytearray'> 351804356720

# for val in lst:
#     print(val)
# # this output we get
# # 10
# # 20
# # 30
# # 50
# # 27
# # 60
# for a in lst:
#         print(a)

#         a[0] = 100
#         print(a) 


lst[0] = 100 # Modifying the content of bytearray --MUTABLE
print(lst,type(lst),id(lst)) # bytearray(b'd\x14\x1e2\x1b<') <class 'bytearray'> 351804356720

for b in lst[::-1]:
    print(b)
# this is output we get 
# 60
# 27
# 50
# 30
# 20
# 100
    