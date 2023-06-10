# Nested or Inner Loops:
__Properties = '''The Process of Defining One Loop inside of another Loop is called Nested OR Inner Loop.

The Execution process of Inner OR nested Loop is that "For Every Value of Outer Loop, Inner Loop executes  
   repeatedly for finite number of times until Inner loop condition becomes false."

In Python Program, we can Loop in 4 Approaches. They are
------------------------------------------------------------------------------------------------------------------------------		
Syntax1: for loop in for loop
----------
			for  Varname1 in Iterable-object1:
			     ------------------------------------
			     ------------------------------------
			     for Varname2 in Iterable-Object2:
			            ------------------------------------
				   ------------------------------------
			     else:
			           ----------------------------------
				   ----------------------------------
		    else:
			    --------------------------------------
			    --------------------------------------
------------------------------------------------------------------------------------------------------------------------------
Syntax2:     while loop in while loop
--------------
			---------------------------------
			while(Test Cond1):
			        --------------------------
				--------------------------
				while(Test Cond2)
				      ------------------------
				      ------------------------
				else:
				      ----------------------------
				      ----------------------------	
			else:
				--------------------------------
				--------------------------------
------------------------------------------------------------------------------------------------------------------------------
Syntax3:     for loop in while loop
--------------
			---------------------------------
			while(Test Cond1):
			        --------------------------
				--------------------------
				for Varname2 in Iterable-Object2:
			           ------------------------------------
				   ------------------------------------
			        else:
			           ----------------------------------
				    ----------------------------------
			else:
				--------------------------------
				--------------------------------
------------------------------------------------------------------------------------------------------------------------------
Syntax1: while loop in for loop
----------
			for  Varname1 in Iterable-object1:
			     ------------------------------------
			     ------------------------------------
			     while(Test Cond2)
				      ------------------------
				      ------------------------
			     else:
				      ----------------------------
				      ----------------------------	
		       else:
				--------------------------------------
				-------------------------------------- '''
# Example:
# Program for demonstrating for loop in for loop
# for i in range(1, 8):
#     print("Outer Loop i is ({})".format(i))
#     print("-----------------------------")
#     for j in range(1, 4):
#         print("\tInner Loop j = ({})".format(j))
#         print("-----------------------------")
#     else:
#         print("-----------------------------")
#         print("I am out from Inner Loop")
#         print("-----------------------------")
# else:
#     print("---------------------------------")
#     print("I am out From Outer Loop")
#     print("-----------------------------")


# Program for demonstrating while loop in while loop
# i = 0
# while i <= 8:
#     print("Outer Loop i is ({})".format(i))
#     print("-----------------------------")
#     j = 1
#     while j <= 4:
#         print("\tInner Loop j = ({})".format(j))
#         print("-----------------------------")
#         j = j + 1
#     else:
#         print("-----------------------------")
#         print("I am out from Inner Loop")
#         i = i + 1
#         print("-----------------------------")
# else:
#     print("---------------------------------")
#     print("I am out From Outer Loop")
#     print("-----------------------------")


# Program for demonstrating while loop in for loop
# for i in range(1, 8):
#     print("Outer Loop i is ({})".format(i))
#     print("-----------------------------")
#     j = 1
#     while j <= 4:
#         print("\tInner Loop j = ({})".format(j))
#         print("-----------------------------")
#         j = j + 1
#     else:
#         print("-----------------------------")
#         print("I am out from Inner Loop")
#         print("-----------------------------")
# else:
#     print("---------------------------------")
#     print("I am out From Outer Loop")
#     print("-----------------------------")


# Program for demonstrating for loop in while loop
# i = 0
# while i <= 8:
#     print("Outer Loop i is ({})".format(i))
#     print("-----------------------------")
#     for j in range(1, 5):
#         print("\tInner Loop j = ({})".format(j))
#         print("-----------------------------")
#
#     else:
#         print("-----------------------------")
#         print("I am out from Inner Loop")
#         print("-----------------------------")
#         i = i + 1
# else:
#     print("---------------------------------")
#     print("I am out From Outer Loop")
#     print("-----------------------------")


#Program for accepting list of numerical Integer values and generates mul tables
# lst = [12, 14, 0, 8, 19, -4, -2, 16]
# for num in lst:
#     if num <= 0:
#         print("{} is Invalid Input".format(num))
#
#     else:
#         print("================================")
#         print("Mul Table for {}".format(num))
#         print("================================")
#         for i in range(1, 11):
#             print("\t{} x {} = {}".format(num, i, num*i))
#
#         else:
#             print("--------------------------------------")


# Program for accepting list of numerical Integer values and generates mul tables
# n = int(input("Enter a Number which you have to generate Mul Table: "))
# if n <= 0:
#     print("{} is Invalid Input".format(n))
#
# else:
#     lst = list()
#     for i in range(1, n + 1):
#         val = int(input("Enter {} Value for Generating Mul Table".format(i)))
#         lst.append(val)
#     else:
#         print("Given Elements {}".format(lst))
#         for num in lst:
#             if num <= 0:
#                 print("{} is Invalid Input".format(num))
#                 print("---------------------------------")
#                 print("Multiple Table for : {}".format(num))
#                 print("---------------------------------")
#             for i in range(1, 11):
#                 print("\t({} x {}) = {}".format(num, i, num*i))
#             else:
#                 print("---------------------------------------")


# Write a Python Program which will generate list of prime numbers with in the given range
# n = int(input("Enter How many Numbers you want to generate: "))
# if n <= 0:
#     print("{} is Invalid Input".format(n))
# else:
#     print("Given Prime Numbers Within {}".format(n))
#     print("-----------------------------------------")
#     for num in range(2, n + 1):
#         res = "PRIME"
#         for i in range(2, num - 1):
#             if num % i == 0:
#                 res = "NOT PRIME"
#                 break
#         if(res == "PRIME"):
#             print("\t{}".format(num))
#     print("------------------------------------------")



# Write a Python Program which will generate list of numerical values and sort those Values in ascendind and Descending Order
# n = int(input("Enter How many Numbers you want to generate: "))
# if n <= 0:
#     print("{} is Invalid Input".format(n))
#
# else:
#     lst = list()
#     for i in range(1, n + 1):
#         val = int(input("Enter {} Values: ".format(i)))
#         lst.append(val)
#     else:
#         print("------------------------------------------------------")
#         print("Given List {}".format(lst))
#         print("------------------------------------------------------")
#         lst.sort()
#         print("------------------------------------------------------")
#         print("List in Ascending Order = {}".format(lst))
#         print("------------------------------------------------------")
#         lst.sort(reverse=True)
#         print("------------------------------------------------------")
#         print("List in Descending Order = {}".format(lst))
#         print("------------------------------------------------------")

# Write a Python Program which will decide weather the Citizen is eligible to vote or not.
# age = int(input("Enter Your Age: "))
# if age < 18:
#     print("You are Not Eligible to Vote")
# else:
#     print("You are Eligible")

#                                               OR
while(True):
    age = int(input("Enter Your Age: "))
    if age >= 18:
        break
    else:
        print("{} is Invalid Age, try again".format(age))

print("{} Years Age Citizen is Eligible to Vote".format(age))











