# 2. if....else statements
___Properties = '''
Syntax :

if (Test Cond):
-----> Statement 1
-----> Statement 1
-----> ___________
-----> Statement-n
else:
-----> Statement 11
-----> Statement 12
-----> ___________
-----> Statement-1n
---------------------------
Other Statements in Programming
____________________________

Explanation: Here if and else are keywords 
             If Test Cond is True then PVM Executes Indentation Block of statements 1  and later executes other statements.
             If the Test Cond is False then PVM Executes  Indentation block of statements 2 and later executes Other statements in program.'''

# Write a python program which will three numerical integer values and decide the biggest among them and check for the Equality by using if....else statements.
num1 = int(input("Enter First Value: "))
num2 = int(input("Enter Second Value: "))
num3 = int(input("Enter Third Value: "))

if (num1 == num2) and (num2 == num3) and (num3 == num1):
    print("All Value are Equal")

else:
    if (num1 >= num2) and (num1 >= num3):
        print("{} is Biggest numerical Value".format(num1))
    else:
        if (num2 > num1) and (num2 >= num3):
            print("{} is Biggest numerical Value".format(num2))
        else:
            if (num2 > num1) and (num2 >= num3):
                print("{} is Biggest numerical Value".format(num2))
            else:
                if (num3 >= num1) and (num3 > num2):
                    print("{} is Biggest numerical Value".format(num3))

# Write a python program which will two numerical integer values and decide the biggest among them and check for the Equality by using if....else statements.
num1 = int(input("Enter First Value: "))
num2 = int(input("Enter Second Value: "))
if (num1 == num2) :
    print("Both Value are Equal")
else:
    if (num1 > num2):
        print("{} is Biggest numerical Value".format(num1))
    else:
        print("{} is Biggest numerical Value".format(num2))


# Write a python program which will accept any digits and print the name of the digits.
dig = int(input("Enter any Digit: "))
if (dig == 0):
    print("{} is One".format(dig))
else:
    if(dig == 1):
        print("{} is One".format(dig))
    else:
        if(dig == 2):
            print("{} is Two".format(dig))
        else:
            if(dig == 3):
                print("{} is Three".format(dig))
            else:
                if(dig == 4):
                    print("{} is Four".format(dig))
                else:
                    if(dig == 5):
                        print("{} is Five".format(dig))
                    else:
                        if(dig == 6):
                            print("{} is Six".format(dig))
                        else:
                            if(dig == 7):
                                print("{} is Seven".format(dig))
                            else:
                                if(dig == 8):
                                    print("{} is Eight".format(dig))
                                else:
                                    if(dig == 9):
                                        print("{} is Nine".format(dig))
                                    else:
                                        if(dig < 0):
                                            print("{} is Negative".format(dig))
                                        else:
                                            if(dig > 9):
                                                print("{} is a Number".format(dig))
print("Program Execution Completed")

# Write a python program which will accept any digits and print the name of the digits by using Ternary Operators.
dig = {0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"}
d = int(input("Enter any Digit: "))
res = dig.get(d) if (dig.get(d) != None) else "a Number"
print("{} is {}".format(d, res))

#                                                          'OR'

dig = {0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"}
d = int(input("Enter any Digit: "))  # d= 0 1 2 3 4 5 6 7 8 9

print("{} is {}".format(d, dig.get(d) if (dig.get(d) != None) else "a Number"))

#                                                          'OR'

dj = {0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE", -1: "-ONE", -2: "-TWO",
    -3: "-THREE", -4: "-FOUR", -5: "-FIVE", -6: "-SIX", -7: "-SEVEN", -8: "-EIGHT", -9: "-NINE"}

dig = int(input("Enter Any Type of Digit: ")) # d = -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9
print("{} is {}".format(dig, dj.get(dig) if (dj.get(dig) != None) else "a Number"))


# Write a Python Programm which wil organize state and capitals and display them Tabler format, accept the state name if the State name present

statescaps = {"TS": "HYD", "KAR": "BANG", "TAMIL": "CHE..", "MH": "MUM", "AP": "VIZ"}
print("-----------------------------------------------")
print("\tState Name\tCapital Name:")
print("-----------------------------------------------")
for states, caps in statescaps.items():
    print("\t{}\t\t{}".format(states,caps))
else:
    print("-----------------------------------------------")
# accept ur state name
stname = input("Enter Ur State Name:")
cap = statescaps.get(stname.lower())
if ( cap == None ):
    print("{} does not Contain Capital".format(stname))
else:
    print("{} and Its Capital is {}".format(stname, cap))

