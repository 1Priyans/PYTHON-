_ = """
Form-1 :	This Form will handle One Exception at a time
------------
            try:
                 --------------------
                 --------------------
            except <exception-class-name>:
            	---------------------------------------
            Block of statements provides
            user-friendly Error Message
			    -------------------------------------"""

# # Example:
# Program for Demonstrating keywords for handling the Exception
# try:
#     a, b = int(input("Enter First Value: ")), int(input("Enter Second Value: "))
#     c = a/b
# except ValueError:
#     print("Don't Enter Alphanumerics, Str and Symbols")
# else:
#     print("Division of ({}/{}) = {}".format(a, b, c))

# Program for Demonstrating keywords for handling the Exception
try:
    a, b = int(input("Enter First Value: ")), int(input("Enter Second Value: "))
    c = a/b
except ZeroDivisionError :
    print("Don't Enter Zero in Denominator")
else:
    print("Division of ({}/{}) = {}".format(a, b, c))