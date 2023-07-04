_ = """
Form-2:      single except blocks handle Multiple Specific Exceptions---Multi Exception handling Block
------------
            try:
                ------------------------------------
                ------------------------------------
                ------------------------------------
            except (exception-class-name1,exception-class-name-2...exception-class-name-n):
                ---------------------------------------
                Block of statements provides
                user-friendly Error Message for all
                exceptions
                -------------------------------------"""

# Example:
# Program for Demonstrating keywords for handling the Exception
try:
    a, b = int(input("Enter First Value: ")), int(input("Enter Second Value: "))
    c = a/b
    d = a + b
except (ZeroDivisionError, ValueError):
    print("Don't Enter Zero in Denominator")
    print("Don't Enter Alphanumerics, Str and Symbols")
else:
    print("Division of ({}/{}) = {}".format(a, b, c))
    print("Addition of ({} + {}) = {}".format(a, b, d))
