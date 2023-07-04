# Program for reading the data from File
try:
    with open("FileWriteEx1.py", "r") as information:
        filedata = information.read()
        print("------------------------------------------")
        print(filedata)
        print("------------------------------------------")
except FileNotFoundError:
    print("File Does not Exist")  # File Does not Exist
