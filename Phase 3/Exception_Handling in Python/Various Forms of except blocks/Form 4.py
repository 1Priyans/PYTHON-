_ = """Form-4:-------> Not Recommended
            try:
                --------------------
                 --------------------
            except : # Default except Block
                ---------------------------------------
                print(alias name)
                -------------------------------------"""
# Example:
# Program for Demonstrating keywords for handling the Exception
try:
    a, b = int(input("Enter First Value: ")), int(input("Enter Second Value: "))
    c = a/b
    d = a + b
except:
    print("OOps Something Went Wrong")
else:
    print("Division of ({}/{}) = {}".format(a, b, c))
    print("Addition of ({} + {}) = {}".format(a, b, d))