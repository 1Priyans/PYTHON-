_ = """
5) w+
------------------------------------------------------------------------------------------------------------------------------------
=>This Mode is used for Creating a File and Opening the File in Write Mode.
=>In Otherwords, If we Open NEW FILE in "w+" Mode Then That File created and Opened in write Mode and we 
    can write the data. If we Open EXISTING FILE in "w+" Mode Then That File  Opened in write Mode and 
    existing data OVERLAPPED with New Data
=>If Open the File in "w+" Then First we have Perform WRITE Operations and later we can perform READ 
   Operation."""
# Example:
# Program Opening the file in r+ Mode
try:
    with open("Stud.data", "w+") as filep:
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