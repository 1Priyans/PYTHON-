# Program for reading the data from File
fname = input("Enter File Name: ")
try:
    with open(fname) as information:
        filedata = information.read()
        print("------------------------------------------")
        print(filedata)
        print("------------------------------------------")
except FileNotFoundError:
    print("File Does not Exist")# Program for reading the data from File
