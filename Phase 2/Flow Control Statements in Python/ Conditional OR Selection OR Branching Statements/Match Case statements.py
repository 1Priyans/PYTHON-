# 4. Match Case Statement:

__Properties = ''' Here "match  case" is one the new feature in Python 3.10 Version onwards

The purpose of match case statement is that "To deal with Pre-defined Test Conditions"

 Syntax:

match(Choice Expr):
	case Choice Label1:
	 Block of Stements-1
	case Choice Label2:
	 Block of Stements-2
	case Choice Label3:
	 Block of Stements-3
	----------------------------
	case Choice Label-n:
	 Block of Stements-n
	case _:	 # Default Case Block
	 default Block of Statements
-------------------------------------------------------
Other Statements in Program
------------------------------------------------------- 

Explanation:

a) Here "match" and "case" are the keywords

b) "Choice Expr" represents either int or str  or bool

c) If "Choice Expr" is matching with "case label1" then PVM executes Block of Statements-1 and later executes Other statements in program.

d) If "Choice Expr" is matching with "case label2" then PVM executes Block of Statements-2 and later executes Other statements in program.

e) In General "Choice Expr" is trying match with case label-1, case label-2,....case label-n then PVM executes corresponding block of statements 
and later executes Other statements in program.

f) If "Choice Expr" is not matching with  any  of the specified case labels then PVM executes Default Block of Staements which are written under 
default case block (case _ ) and later executes Other statements in program.

g) Writing default case block is optional and If we write then it must be written at last (Otherwise we get SyntaxError)

h) When we represent multiple case labels under one case then those case labels must be combined with Bitwise OR Operator ( | )  .'''

# Example:

__ques = '''
1.) Write a python program which will implement the following
---------------------------------------------------------
                Arithmatic operations 
---------------------------------------------------------
                 1. Addition 
                 2. Subtraction
                 3. Multiplication
                 4. Division
                 5. Modulo Division
                 6. Exponentiation
                 7. Exit
----------------------------------------------------------
Enter Your Choice:  
----------------------------------------------------------'''
# Programming for Performing Arithmatic Operation by using match case statement.
import sys
print("---------------------------------------------------------")
print("\tArithmatic Operation" )
print("---------------------------------------------------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo Division")
print("6. Exponentiation")
print("7. Exit")
print("---------------------------------------------------------")

ch = int(input("Enter Your Choice: "))
match(ch):
    case 1:
        print("Enter Two values for Addition: ")
        a, b = float(input()), float(input())
        print("\tAdd({}, {}) = {}".format(a, b, a + b))

    case 2:
        print("Enter Two values for Subtraction: ")
        a, b = float(input()), float(input())
        print("\tSub({}, {}) = {}".format(a, b, a - b))

    case 3:
        print("Enter Two values for Multiplication: ")
        a, b = float(input()), float(input())
        print("\tMul({}, {}) = {}".format(a, b, a * b))

    case 4:
        print("Enter Two values for Division: ")
        a, b = float(input()), float(input())
        print("\tDiv({}, {}) = {}".format(a, b, a / b))

    case 5:
        print("Enter Two values for Modulo Division: ")
        a, b = float(input()), float(input())
        print("\tSub({}, {}) = {}".format(a, b, a // b))

    case 6:
        print("Enter Two values for Exponentiation: ")
        a, b = float(input()), float(input())
        print("\tSub({}, {}) = {}".format(a, b, a ** b))

    case 7:
        print("Thanks for Using this Program:  ")
        sys.exit()

    case _:
        print("Ur Selection of Operation is wrong-try again")

print("------------------------------------------------------")



_ques = '''
1.) Write a python program which will implement the following
---------------------------------------------------------
                Area of Different Figures 
---------------------------------------------------------
                 C. Circle
                 R. Rectangle
                 S. Square,Circle
                 T. Triangle
                 E. Exit                 
----------------------------------------------------------
Enter Your Choice:  
----------------------------------------------------------'''
# Programming for Cal Area of diff figures by using match case statement>
import sys
print("---------------------------------------------------------")
print("\tArea of Different Figures")
print("---------------------------------------------------------")
print("C. Circle")
print("R. Rectangle")
print("S. Square,Circle")
print("T. Triangle")
print("E. Exit")
print("---------------------------------------------------------")

ch = input("Enter Your Choice: ").upper()
match(ch):
    case "C":
        rad = float(input("Enter Radius: "))
        ar = 3.14 * rad**2
        print("\tArea of Circle ({}) = {}".format(rad, ar))

    case "R":
        a = float(input("Enter Length: "))
        b = float(input("Enter Breadth: "))
        ar = a * b
        print("\tArea of Rectangle ({}, {}) = {}".format(a, b, ar))

    case "S":
        s = float(input("Enter Side: "))
        ar = s ** 2
        print("\tArea of Square,Circle ({}) = {}".format(s, ar))

    case "T":
        b = float(input("Enter Base: "))
        h = float(input("Enter Height: "))
        ar = b * h
        print("\tArea of Triangle ({}, {}) = {}".format(b, h, ar))

    case "E":
        print("Thanks for this program")
        sys.exit()

    case _:
        print("Ur Selection of Operation is Wrong Please Try again")

print("--------------------------------------------------------------")


_quest = '''
1.) Write a python program which will implement the following
---------------------------------------------------------
                Area of Different Figures 
---------------------------------------------------------
                 C. Circle
                 R. Rectangle
                 S. Square,Circle
                 T. Triangle
                 E. Exit                 
----------------------------------------------------------
Enter Your Choice:  
----------------------------------------------------------'''
# Programming for Cal Area of diff figures Multiple at a time by using match case statement
import sys

while True:

    print("---------------------------------------------------------")
    print("\tArea of Different Figures")
    print("---------------------------------------------------------")
    print("C. Circle")
    print("R. Rectangle")
    print("S. Square,Circle")
    print("T. Triangle")
    print("E. Exit")
    print("---------------------------------------------------------")
    ch = input("Enter Your Choice: ").upper()
    match ch:
        case "C":
            rad = float(input("Enter Radius: "))
            ar = 3.14 * rad**2
            print("\tArea of Circle ({}) = {}".format(rad, ar))

        case "R":
            a = float(input("Enter Length: "))
            b = float(input("Enter Breadth: "))
            ar = a * b
            print("\tArea of Rectangle ({}, {}) = {}".format(a, b, ar))

        case "S":
            s = float(input("Enter Side: "))
            ar = s ** 2
            print("\tArea of Square,Circle ({}) = {}".format(s, ar))

        case "T":
            b = float(input("Enter Base: "))
            h = float(input("Enter Height: "))
            ar = b * h
            print("\tArea of Triangle ({}, {}) = {}".format(b, h, ar))

        case "E":
            print("Thanks for using this program")
            sys.exit()

        case _:
            print("Ur Selection of Operation is Wrong Please Try again")

    print("--------------------------------------------------------------")


__quest1 = '''
1.) Write a python program which will implement the Working schedule of classes Which is following
---------------------------------------------------------
               Working and Weekend Schedule of classes   
---------------------------------------------------------
                            MONDAY
                            TUESDAY
                            WEDNESDAY
                            THURSDAY
                            FRIDAY
                            SATURDAY
                            SUNDAY
                            EXIT                
----------------------------------------------------------
Enter Your Choice:  
---------------------------------------------------------- '''
# Programming for Match Case Statement
import sys

print("---------------------------------------------------------")
print("\tWorking and Weekend Schedule of classes")
print("---------------------------------------------------------")
print("\t MONDAY")
print("\t TUESDAY")
print("\t WEDNESDAY")
print("\t THURSDAY")
print("\t FRIDAY")
print("\t SATURDAY")
print("\t SUNDAY")
print("\t EXIT")
print("---------------------------------------------------------")

wkd = (input("Enter the Week name: ").upper())
match wkd:
    case "MONDAY":
        print("{} is Working Day:".format(wkd))

    case "TUESDAY":
        print("{} is Working Day:".format(wkd))

    case "WEDNESDAY":
        print("{} is Working Day:".format(wkd))

    case "THURSDAY":
        print("{} is Working Day:".format(wkd))

    case "FRIDAY":
        print("{} is Working Day:".format(wkd))

    case "SATURDAY":
        print("{} is Week End preparing UGAC Plans:".format(wkd))

    case "SUNDAY":
        print("{} is Holiday Day for Resting :".format(wkd))

    case _:
        print("{} is not a week Day--> plz learn spelling week days".format(wkd))


#                                                          OR

# Program For Match Case Statement by using Bitwise OR '|' Operator
wkd = input("Enter the week name:").upper()
match (wkd):
    case "MONDAY" | "TUESDAY" | "WEDNESDAY" | "THURSDAY" | "FRIDAY":
        print("{} is Working Day:".format(wkd))

    case "SATURDAY":
        print("{} is Week End preparing UGAC Plans:".format(wkd))

    case "SUNDAY":
        print("{} is Holiday Day for resting :".format(wkd))

    case _:
        print("{} is not a week Day--plz learn spelling week days".format(wkd))



# Program For Match Case Statement including if....else.

wkname = input("Enter Week Name: ").upper()
if wkname in ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]:
    match (wkname[0: 3]):
        case "MON" | "TUE" | "WED" | "THU" | "FRI":
            print("{} is Working Day".format(wkname))

        case "SAT":
            print("{} is Week End preparing UGAC Plans:".format(wkname))

        case "SUN":
            print("{} is Holiday for Resting".format(wkname))

else:
    print("{} is not a week Day--plz learn spelling week days".format(wkname))


__quest = '''
1.) Write a python program which will convert diff temperatures from one scale to another scale.
---------------------------------------------------------
               List of Converting Different Temperature   
---------------------------------------------------------
                1. Celsius to Kelvin
                2. Kelvin to Celsius
                3. Fahrenheit to Celsius
                4. Celsius to Fahrenheit
                5. Fahrenheit to Kelvin
                6. Kelvin to Fahrenheit       
                7. Exit
----------------------------------------------------------
Enter Your Choice:  
---------------------------------------------------------- '''
import sys
while True:
        # print("---------------------------------------------------------")
        # print("\tList of Converting Different Temperature ")
        # print("---------------------------------------------------------")
        # print("\t1. Celsius to Kelvin")
        # print("\t2. Kelvin to Celsius")
        # print("\t3. Fahrenheit to Celsius")
        # print("\t4. Celsius to Fahrenheit")
        # print("\t5. Fahrenheit to Kelvin")
        # print("\t6. Kelvin to Fahrenheit ")
        # print("\t7. Exit")
        # print("---------------------------------------------------------")

        temp = float(input("Enter Number According the list: "))

        match temp:
            case 1:
                cel = float(input("Enter the Value in Celsius: "))
                cel_to_kel = cel + 273.15
                print("The Value of {} into Kelvin is {}".format(cel, cel_to_kel))

            case 2:
                kel = float(input("Enter the Value in Kelvin: "))
                kel_to_cel = kel - 273.15
                print("The Value of {} into Celsius is {}".format(kel, kel_to_cel))

            case 3:
                fahr = float(input("Enter the Value in Fahrenheit: "))
                fahr_to_cel = (fahr - 32) * (5/9)
                print("The Value of {} into Celsius is {}".format(fahr, fahr_to_cel))

            case 4:
                cel = float(input("Enter the Value in Celsius: "))
                cel_to_fahr = cel * (9/5) + 32
                print("The Value of {} into Fahrenheit is {}".format(cel, cel_to_fahr))

            case 5:
                fahr = float(input("Enter the Value in Fahrenheit: "))
                fahr_to_kel = (fahr - 32) * (5/9) + 273.15
                print("The Value of {} into Kelvin is {}".format(fahr, fahr_to_kel))

            case 6:
                kel = float(input("Enter the Value in Kelvin: "))
                kel_to_fahr = (kel - 273.15) * (9/5) + 32
                print("The Value of {} into Fahrenheit is {}".format(kel, kel_to_fahr))

            case 7:
                print("Thanks for using this Program")
                sys.exit()

            case _:
                print("Ur Selection of Operation is Wrong Please Try again")

        print("-------------------------------------------------------------------")

