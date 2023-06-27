# Program for accepting Two Numerical Integer values and find their Division
try:
    print("Program Execution Started")
    s1 = input("Enter First Value: ")
    s2 = input("Enter Second Value: ")
    # Convert str  data into int type
    a = int(s1)
    b = int(s2)
    # Calculating Division of Two Numbers
    c = a / b

except ValueError:
    print("Do not Enter  AlphaNumeric, Str and Symbols")
except ZeroDivisionError:
    print("Do Not Enter Zero in Denominator")

else:
    print("Else Block ----> Result Block")
    print("Division of {}/{} = {}".format(a, b, c))
    print("Program Execution Ended")

finally:
    print("I am from finally Block")