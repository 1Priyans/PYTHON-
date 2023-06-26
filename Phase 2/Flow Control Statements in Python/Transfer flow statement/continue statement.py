# Continue statement
__Properties = ''' continue is a keyword

continue statement is used for making the PVM to go to the top of the loop without executing the following statements 
which are written after continue statement for that current Iteration only.

continue statement  to be used always inside of loops.

when we use continue statement inside of loop then else part of corresponding loop also executes provided loop 
condition becomes false.
-----------------
=>Syntax:-
----------------
for varname   in Iterable-object:
------------------------------------------
    if ( Test Cond):
        continue 
    statement-1  # written after continue statement
    statement-2
    statement-n
    -----------------------------------------			
    -----------------------------------------

=>Syntax:-
----------------
while (Test Cond):
 ------------------------------------------			    
    if ( Test Cond):
        continue 			    
    statement-1  # written after continue stateemnt
    statement-2
    statement-n
-----------------------------------------
-----------------------------------------'''

# Example :

# Program for demonstrating constinue statement--> for loop
# s = "ROSSUM"
# for i in s:
#     if i == "S":
#         continue
#     print("\t{}".format(i))
# else:
#     print("___________________________________")

# Program for demonstrating constinue statement--> While loop
# s = "ROSSUM"
# print("___________________________________")
# print("By using While Loop")
# print("___________________________________")
# i = 0
# while (i < len(s)):
#     if s[i] == "O":
#         i = i + 1
#         continue
#     print("\t{}".format(s[i]))
#     i = i + 1
# else:
#     print("========================================")



# # Program for demonstrating constinue statement--> for loop
# s = "ROSSUM"
# for i in s:
#     if i == "S" or i == "R":
#         continue
#     print("\t{}".format(i))
# else:
#     print("___________________________________")

# Program for demonstrating constinue statement--> for loop
# s = "ROSSUM"
# print("By Using While Loop")
# i = 0
# while i < len(s):
#     if s[i] == "R" or s[i] == "U":
#         i = i + 1
#         continue
#
#     print("\t{}".format(s[i]))
#     i = i + 1
# else:
#     print("___________________________________")


# Write a Python Program which will accepting list of numbers and find Maximum and Minimum Number.
# n = int(input("Enter How Numerical Values you have: "))
# if n <= 0:
#     print("{} is Invalid Input".format(n))
# else:
#     lst = list()
#     print("Enter {} Values".format(n))
#     for i in range(1, n + 1):
#         lst.append(float(input()))
#     else:
#         print("------------------------------------")
#         print("Given list {}".format(lst))
#         print("------------------------------------")
#         print("Maximum Element ({}) = {}".format(lst, max(lst)))
#         print("Minium Element ({}) = {}".format(lst, min(lst)))


# Write a Python Program which will accepting list of numbers and find Maximum and Minimum Number Without using max() and min() Function.
# n = int(input("Enter How Numerical Values you have: "))
# if n <= 0:
#     print("{} is Invalid Input".format(n))
# else:
#     lst = list()
#     print("Enter {} Values".format(n))
#     for i in range(1, n + 1):
#         lst.append(float(input()))
#
#     else:
#         print("-----------------------------------------------------------")
#         print("Given list = {}".format(lst))
#         print("-----------------------------------------------------------")
#         maxn = lst[0]
#         minn = lst[0]
#         for i in range(1, len(lst) + 1):
#             if (lst[i] > maxn):
#                     maxn = lst[i]
#             elif (lst[i] < minn):
#                     minn = lst[i]
#         else:
#             print("Max Element ({}) = {}".format(lst, maxn))
#             print("Min Element ({}) = {}".format(lst, minn))

# Program for accepting List of numbers and find sum of +ve and -ve separately.


# Program for accepting List of numbers and find sum of +ve and -ve separately.
# lst = [10, 20, -30, 40, -15, -25, 25, 0, -35]
# print("=====================================")
# print("Given List {}".format(lst))
# print("=====================================")
# print("--------------------------------------")
# print("List of Positive Values")
# print("--------------------------------------")
# pssum = 0
# for val in lst:
#     if val <= 0:
#         continue
#     print("\t{}".format(val))
#     pssum = pssum + val
# else:
#     print("Sum of Positive Elements is {}".format(pssum))
#     print("---------------------------------------------")
#     print("List of Negative Values")
#     print("---------------------------------------------")
#     ngsum = 0
#     for val in lst:
#         if val >= 0:
#             continue
#         print("\t{}".format(val))
#         ngsum = ngsum + val
#     else:
#         print("Sum of Negative Elements is {}".format(ngsum))

#
# n = int(input("Enter How many Numerical Values u have:"))
# if(n <= 0):
#     print("{} is invalid Input".format(n))
# else:
#     lst=list()  # OR  lst=[]<----creating empty list
#     for i in range(1,n+1):
#         val = float(input("Enter {} Value:".format(i)))
#         lst.append(val)
#     else:
#         print("-------------------------------------------")
#         print("Given List:{}".format(lst)) # [10.0, 15.0, -35.0, -15.0, -67.0, 34.5, 8.9, -4.5, -1.2, 35.0]
#         print("-------------------------------------------")
#         #prepare +ve list data
# 		pslist = []
#         for val in lst:
#             if(val<=0):
#                 continue
# 			pslist.append(val)
# 		else:
# 			print("Possitive List of Elements={}".format(pslist))
# 			#prepare -ve list data
# 			nslist=[]
# 			for val in lst:
# 				if(val>=0):
# 					continue
# 				nslist.append(val)
# 			else:
# 				print("-------------------------------------------")
# 				print("Negaticve List of Elements={}".format(nslist))
# 				print("=======================================")
# 				print("Posstive Sum List({})={}".format(pslist,sum(pslist)))
# 				print("Negative Sum List({})={}".format(nslist,sum(nslist)))
# 				print("=======================================")


















