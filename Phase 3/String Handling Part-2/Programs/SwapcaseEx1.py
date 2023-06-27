# Program for Performing swap case of str data without using Swapcase() function
strdata = input("enter a Line of Text: ")  # PyThOn
print("Given Data = {}".format (strdata))
s = ""
for ch in strdata:
    if ch.isupper():
        s = s + ch.lower()
    elif ch.islower():
        s = s + ch.upper()
print("Swapcase Data = {}".format(s))  # pYtHoN
