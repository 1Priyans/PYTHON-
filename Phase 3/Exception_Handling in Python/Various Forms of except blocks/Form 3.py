_ = """
Form-3:    This Form will handle One Exception at a time with alias name and It captures Technical Error Message pertticular 
           exception
----------------
            try:
                --------------------
                --------------------
            except <exception-class-name> as alias name:
                ---------------------------------------
                print(alias name)
				-------------------------------------"""

# Example:
# Program for Demonstrating keywords for handling the Exception
try:
    a, b = int(input("Enter First Value: ")), int(input("Enter Second Value: "))
    c = a/b
    d = a + b
except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
else:
    print("Division of ({}/{}) = {}".format(a, b, c))
    print("Addition of ({} + {}) = {}".format(a, b, d))
