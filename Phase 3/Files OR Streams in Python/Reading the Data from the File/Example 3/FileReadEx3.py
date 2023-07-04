# Program for reading the data from File
fname = input("Enter File Name: ")
try:
    with open(fname) as information:
        filedata = information.readlines()
        print("------------------------------------------")
        for val in filedata:
            print(val)
        print("------------------------------------------")
except FileNotFoundError:
    print("File Does not Exist")