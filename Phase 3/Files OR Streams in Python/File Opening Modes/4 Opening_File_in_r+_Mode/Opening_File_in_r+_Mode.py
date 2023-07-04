_ = '''
4) r+
------------------------------------------------------------------------------------------------------------------------------------
=>This Mode is used for Opening the File in Read Mode.
=>If we Open the file Name in "r+" Mode and If the file name does not exist then we get FileNotFoundError.
=>If we Open the file in "r+" Mode then First We can Perform READ Operations and Later we can also Perform Write Operation.'''

# Program Opening the file in r+ Mode
try:
    with open("Stud.data", "r+") as filep:
        print("----------------------------------------------")
        print("----------Inside of with open() as------------------------------")
        print("File Opened in Read Mode")
        print("Type of filep = {}".format(type(filep)))
        print("Name of the File: ", filep.name)
        print("File Mode Name:", filep.mode)
        print("Is File Active:", filep.closed)
        print("Is File Readable:", filep.readable())
        print("Is File Writable:", filep.writable())
        print("----------------------------------------------")
        print("*******Out of with open() as ***********")
        print("Is File Active:", filep.closed)

except FileNotFoundError:
    print("File Does not Exist")
