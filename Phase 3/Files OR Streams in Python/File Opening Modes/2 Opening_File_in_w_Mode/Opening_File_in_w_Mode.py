_ = '''
2. w
------------------------------------------------------------------------------------------------------------------------------------
=>This Mode is used for Creating a File and Opening the File in Write Mode.
=>In Otherwords, If we Open NEW FILE in "w" Mode Then That File created and Opened in write Mode and we can write the data. 
If we Open EXISTING FILE in "w" Mode Then That File  Opened in write Mode and existing data OVERLAPPED with New Data'''
# Example:
# Program Opening the file in Read Mode
filep = open("Student.data", "w")
print("----------------------------------------------")
print("File Created and Opened in Write Mode")
print("Type of filep = {}".format(type(filep)))
print("Name of the File: ", filep.name)
print("File Mode Name:", filep.mode)
print("Is File Active:", filep.closed)
print("Is File Readable:", filep.readable())
print("Is File Writable:", filep.writable())
print("----------------------------------------------")
