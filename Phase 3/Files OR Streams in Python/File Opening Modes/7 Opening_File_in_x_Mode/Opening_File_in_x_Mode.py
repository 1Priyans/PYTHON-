_ = '''
7) x
------------------------------------------------------------------------------------------------------------------------------------
=>This Mode is used for Creating and Opening the File Name Once at a time in Write Mode eXclusively and we 
    can peform only Write Operations.
=>Once we Open the Exiting File Name in "x" mode  then we get FileExistError.'''
# Example:
try:
    with open("Student2.data", "x") as fp:
        print("==================================================")
        print("----------Inside of with open() as------------------------------")
        print("File Opened in Write Mode")
        print("Type of File: ",type(fp))
        print("Name of the File: ",fp.name)
        print("Is File Active",fp.closed)
        print("Is File Redable",fp.readable())
        print("Is File Writable",fp.writable())
    print("*******Out of with open() as ***********")
    print("Is File Active:",fp.closed)
except FileExistsError:
    print("File Already Exist")
