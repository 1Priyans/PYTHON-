# Program for Performing capitalize Operation of str data without using capitalize() Function.
strdata = input("Enter a line of Text: ")  # python is an oop lang
print("Given Data = {}".format(strdata))
ch = strdata[0].upper()
redata = strdata[1:]
capadata = ch + redata
print("Capitalize Data = {}".format(capadata))  # Python is an oop lang