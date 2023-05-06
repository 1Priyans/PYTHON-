# number1 = int(input("Enter your age : "))
# number2 = int(input("Enter your age : "))
# number3 = int(input("Enter your age : "))
# number4 = int(input("Enter your age : "))

# if(number1>number4):
#     f1 = number1
# else:
#     f1 = number4

# if(number2>number3):
#     f2 = number2
# else:
#     f2 = number3

# if(f1>f2):
#     print(str(f1) + "is greatest")
# else:
#     print(str(f2) + "is greatest")

# sub1 = int(input("Enter Your first subject marks: "))
# sub2 = int(input("Enter Your second subject marks: "))
# sub3 = int(input("Enter Your third subject marks: "))

# if(sub1<33 or sub2<33 or sub3>33):
#     print("you are fail")
# elif(sub1 + sub2 + sub3)/3 <= 40:
#     print("you are failed")
# else:
#     print("you passed the test")

# name = input("enter you name \n ")
# if(len(name)<10):
#     print(" your name is correct ")
# else:
#     print("your name is too long")

# names = ["Akash", "Deepak", "Priyansh", "Paras", "yogendra"]
# name = input("enter your name ")
# if name in names:
#     print("your name is present in the the list")
# else:
#     print("your name is not present in the list")

# i = 1

# while i <= 51:
    
#     i = i + 1
#     print(i)

# i = 0
# while (i < 5):
#     print("priyansh")
#     i = i + 1

#For loop method
# fruits = ['Pinapple', 'Apple', 'Banana', 'Mangoes']
# for fruit in fruits:
#     print(fruit)

#for range function in loops 
# for i in range(51, 52):
#     print(i)
# else:
#     print("done")

# num = int(input("Enter number ",))
# for i in range(1, 11):
#     #print(str(num) + "X" + str(i) + "=" + str(i*num)) 
#     print(f"{num} X {i} = {num*i}") # f string method

#While loop method
# fruits = ['Pinapple', 'Apple', 'Banana', 'Mangoes']
# i = 0
# while i<len(fruits):
#     print(fruits[i])
#     i = i + 1

# l1 = ['Priyansh', 'Sohan', 'Sachin', 'Rahul']
# for name in l1:
#     if name.startswith("S"):
#         print("Hello "  + name)

# i = 0
# l1 = ['Priyansh', 'Sohan', 'Sachin', 'Rahul']
# while  i<len(l1):
#     if l1 [i].startswith('S'):
#         print("Hello " + l1[i])
#         i = i + 1

# n =3
# for i in range(3):
#     print(" "  * (n-i-1), end='')
#     print("*" * (2*i+1), end='')
#     print(" "  * (n-i-i))

# n = 3
# for i in range (4):
#     print(" " * (n-i-3), end="")
#     print(" " * (n-i-1), end="")
#     print(" " * (n-i-3))
    

# rows = int(input("Please Enter the Total Number of Rows  : "))

# print("Right Angled Triangle Star Pattern") 
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print('* ', end = '  ')

import cmath
print(cmath.sqrt(-25))




