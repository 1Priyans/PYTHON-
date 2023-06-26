# 3. if..elif...else statements

___Properties = '''
Syntax :

if (Test Cond 1):
-----> Block of Statement 1
elif (Test Cond 2):
-----> Block of Statement 2
elif (Test Cond 3):
-----> Block of Statement 3
--------------------------
--------------------------
elif (Test Cond n):
-----> Block of Statement n
else:
-----> else Block of Statements
-----> Statement 12
---------------------------
Other Statements in Program
____________________________

Explanation: Here if, elif  and else are keywords 
             
             If Test Cond 1 is True then PVM Executes Indentation Block of statements 1  and later executes other statements.
             
             If the Test Cond 1 is False and if the Test Condition 2 is then PVM Executes Indentation block of statements 2 and later executes 
             Other statements in program.
             
             This process will be repeated until all Test conditions are evaluated and all the Test condition are False then PVM Executes Else
             Block of statements and other statements in the program
             
             Writting else Block is Optional.'''

# Example

# Write a python program for accepting any type of digit and display its name by using if..elif..else statement
d = int(input("Enter any Digit:")) # d= 0 1 2 3 4 5 6 7 8 9  123
if(d == 0):
    print("{} is ZERO".format(d))
elif(d == 1):
    print("{} is ONE".format(d))
elif(d == 2):
    print("{} is TWO".format(d))
elif(d == 3):
    print("{} is THREE".format(d))
elif( d== 4):
    print("{} is FOUR".format(d))
elif(d == 5):
    print("{} is FIVE".format(d))
elif(d == 6):
    print("{} is SIX".format(d))
elif(d == 7):
    print("{} is SEVEN".format(d))
elif(d == 9):
    print("{} is NINE".format(d))
elif(d == 8):
    print("{} is EIGHT".format(d))
elif(d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]):
    print("{} is -Ve Digit".format(d))
elif (d > 9) or (d < 0):
    print("{} is NUMBER".format(d))
print("Program execution completed")




