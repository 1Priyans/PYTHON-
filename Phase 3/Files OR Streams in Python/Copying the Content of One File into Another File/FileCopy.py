# Write a Python Program will copy the Content of one file into another
sfile = input("Enter Source File: ")
try:
    with open(sfile, "r") as srcfile:
        dfile = input("Enter Destination File: ")
        with open(dfile, "a") as dstfile:
            sourcefile = srcfile.read()  # Reading Complete Data from the Source File
            dstfile.write(sourcefile)  # Writing the Data of Source File to Destination File
except FileNotFoundError:
    print("File Does not Exist")

