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
for i in range(1, 8):
    print("Outer Loop i is ({})".format(i))
    print("-----------------------------")
    for j in range(1, 4):
        print("\tInner Loop j = ({})".format(j))
        print("-----------------------------")
    else:
        print("-----------------------------")
        print("I am out from Inner Loop")
        print("-----------------------------")
else:
    print("---------------------------------")
    print("I am out From Outer Loop")
    print("-----------------------------")


# Program for demonstrating while loop in while loop
i = 0
while i <= 8:
    print("Outer Loop i is ({})".format(i))
    print("-----------------------------")
    j = 1
    while j <= 4:
        print("\tInner Loop j = ({})".format(j))
        print("-----------------------------")
        j = j + 1
    else:
        print("-----------------------------")
        print("I am out from Inner Loop")
        i = i + 1
        print("-----------------------------")
else:
    print("---------------------------------")
    print("I am out From Outer Loop")
    print("-----------------------------")


# Program for demonstrating while loop in for loop
for i in range(1, 8):
    print("Outer Loop i is ({})".format(i))
    print("-----------------------------")
    j = 1
    while j <= 4:
        print("\tInner Loop j = ({})".format(j))
        print("-----------------------------")
        j = j + 1
    else:
        print("-----------------------------")
        print("I am out from Inner Loop")
        print("-----------------------------")
else:
    print("---------------------------------")
    print("I am out From Outer Loop")
    print("-----------------------------")


# Program for demonstrating for loop in while loop
i = 0
while i <= 8:
    print("Outer Loop i is ({})".format(i))
    print("-----------------------------")
    for j in range(1, 5):
        print("\tInner Loop j = ({})".format(j))
        print("-----------------------------")

    else:
        print("-----------------------------")
        print("I am out from Inner Loop")
        print("-----------------------------")
        i = i + 1
else:
    print("---------------------------------")
    print("I am out From Outer Loop")
    print("-----------------------------")


#Program for accepting list of numerical Integer values and generates mul tables
lst = [12, 14, 0, 8, 19, -4, -2, 16]
for num in lst:
    if num <= 0:
        print("{} is Invalid Input".format(num))

    else:
        print("================================")
        print("Mul Table for {}".format(num))
        print("================================")
        for i in range(1, 11):
            print("\t{} x {} = {}".format(num, i, num*i))

        else:
            print("--------------------------------------")


# Program for accepting list of numerical Integer values and generates mul tables
n = int(input("Enter a Number which you have to generate Mul Table: "))
if n <= 0:
    print("{} is Invalid Input".format(n))

else:
    lst = list()
    for i in range(1, n + 1):
        val = int(input("Enter {} Value for Generating Mul Table".format(i)))
        lst.append(val)
    else:
        print("Given Elements {}".format(lst))
        for num in lst:
            if num <= 0:
                print("{} is Invalid Input".format(num))
                print("---------------------------------")
                print("Multiple Table for : {}".format(num))
                print("---------------------------------")
            for i in range(1, 11):
                print("\t({} x {}) = {}".format(num, i, num*i))
            else:
                print("---------------------------------------")


# Write a Python Program which will generate list of prime numbers with in the given range
n = int(input("Enter How many Numbers you want to generate: "))
if n <= 0:
    print("{} is Invalid Input".format(n))
else:
    print("Given Prime Numbers Within {}".format(n))
    print("-----------------------------------------")
    for num in range(2, n + 1):
        res = "PRIME"
        for i in range(2, num - 1):
            if num % i == 0:
                res = "NOT PRIME"
                break
        if(res == "PRIME"):
            print("\t{}".format(num))
    print("------------------------------------------")



# Write a Python Program which will generate list of numerical values and sort those Values in ascendind and Descending Order
n = int(input("Enter How many Numbers you want to generate: "))
if n <= 0:
    print("{} is Invalid Input".format(n))

else:
    lst = list()
    for i in range(1, n + 1):
        val = int(input("Enter {} Values: ".format(i)))
        lst.append(val)
    else:
        print("------------------------------------------------------")
        print("Given List {}".format(lst))
        print("------------------------------------------------------")
        lst.sort()
        print("------------------------------------------------------")
        print("List in Ascending Order = {}".format(lst))
        print("------------------------------------------------------")
        lst.sort(reverse=True)
        print("------------------------------------------------------")
        print("List in Descending Order = {}".format(lst))
        print("------------------------------------------------------")

# Write a Python Program which will decide weather the Citizen is eligible to vote or not.
age = int(input("Enter Your Age: "))
if age < 18:
    print("You are Not Eligible to Vote")
else:
    print("You are Eligible")

#                                               OR
while(True):
    age = int(input("Enter Your Age: "))
    if 18 <= age <= 100:
        break
    else:
        print("{} is Invalid Age, try again".format(age))

print("{} Years Age Citizen is Eligible to Vote".format(age))


__Ques = '''Write a python program which will implement the following problem:
a) Accept student Number, Student Name and Marks in 3 Sub(C, C++, Python

b) Compute total marks and Percentages of marks

c) Give the student grade as fail provided student secures less than 40 any one the subject.

d) Give the student grade as "DISTINCTION" provided total marks ranges from 250 and 300 (Included).

e) Give the student grade as "First" provided total marks ranges from 200 and 249 (Included)

f) Give the student grade as "Second" provided total marks ranges from 150 and 199 (Included)

g) Give the student grade as "Third" provided total marks ranges from 120 and 149 (Included).'''

# Program for Generating Student Marks Report
# Accept Student Number-- 1 to 100
while True:
    sno = int(input("Enter Student Number (1 - 100): "))
    if 1 <= sno <= 100:
        break
    else:
        print("{} is Invalid Student Number Please Try again".format(sno))

# Accept student Name
sname = input("Enter Student Name: ")

# Accept Student Marks in C (0 to 100)
while True:
    cmrks = int(input("Enter Your Numbers in C: "))
    if 0 <= cmrks < 100:
        break
    print("{} in Invalid Input, try again".format(cmrks))

# # Accept Student Marks in C++ (0 to 100)
while True:
    cpp = int(input("Enter Your Numbers in C++: "))
    if 0 <= cpp < 100:
        break
    print("{} in Invalid Input, try again".format(cpp))

# Accept Student Marks in Python (0 to 100)
while True:
    pyth = int(input("Enter Your Numbers in Python: "))
    if 0 <= pyth <= 100:
        break
    print("{} in Invalid Input, try again".format(pyth))

# Compute total marks and percentage
totalmrks = cmrks + cpp + pyth
percentg = round(totalmrks/3, 2) # round() for finding nearest value of any floating point value

# #Give the student grade as FAIL provided Student Secures Less than 40 any one of the subject.
if cmrks < 40 or cpp < 40 or pyth < 40:
    grade = "FAIL"
else:
    if 250 <= totalmrks <= 300:
        grade = "DISTINCTION"
    elif 200 <= totalmrks <= 249:
        grade = "FIRST"
    elif 150 <= totalmrks <= 199:
        grade = "SECOND"
    elif 120 <= totalmrks <= 149:
        grade = "THIRD"

# Display Marks Report
print("----------------------------------------------------------------------")
print("\t\t\t\tStudent Marks Report")
print("----------------------------------------------------------------------")
print("\tStudent Number: {}".format(sno))
print("\tStudent Name: {}".format(sname))
print("\tStudent Marks in C: {}".format(cmrks))
print("\tStudent MArks in C++ {}".format(cpp))
print("\tStudent Marks in PYTHON: {}".format(pyth))
print("----------------------------------------------------------------------")
print("\tStudent Total Marks: {}".format(totalmrks))
print("\tPercentages : {}".format(percentg))
print("\tStudent Grade: {}".format(grade))


# Write a python program which will accept numerical integer value and find the sum of its Digits.
n = int(input("Enter a Number you want find a Sum of its Digits: "))
if n <= 0:
    print("{} is Invalid Input".format(n))

else:
    s = 0
    tn = n  # Here we are pre-serving original n value in another variable tn
    while n > 0:
        r = n % 10  # This is for getting Digits
        s = s + r  # This is for Addition of digits one by one of a given number
        n = n // 10 # This is for sepreation  if digits like 23234 then 2323 then 232 then 23 and then 2
    else:
        print("Digits Sum of ({}) = {}".format(tn, s))


# Program for accepting a numerical Integer values and find its digits sum
n = int(input("Enter any Number:"))
if(n <= 0):
    print("{} is invalid input".format(n))
else:
    s = 0
    gn = str(n)
    for d in gn:
        x = int(d)
        if(x % 2 == 0):
            s = s+x
    else:
        print("EvenDigitsSum({})={}".format(gn,s))


# Program for accepting a numerical Integer value and decide whether it is Amstrong or not (Amsrong = Sum of Cubes of Digits of given number
n = int(input("Enter any Number:"))
if (n <= 0):
    print("{} is invalid input".format(n))
else:
    s = 0
    tn = n  # Here we are pre-serving original n value in another variable tn
    while (n > 0):
        r = n % 10
        s = s + r ** 3
        n = n // 10
    else:
        if (s == tn):
            print("{} is Amstrong".format(tn))
        else:
            print("{} is Not Amstrong".format(tn))






