_ = '''
3) a
------------------------------------------------------------------------------------------------------------------------------------
=>This Mode is used for Creating a File and Opening the File in Write Mode.
=>In Otherwords, If we Open NEW FILE in "a" Mode Then That File created and Opened in write Mode and we can write the data. 
If we Open EXISTING FILE in "a" Mode Then That File  Opened in write Mode and New Data APPENDED at the end of Existing data.'''
# Example
# Program Opening the file in Append Mode
filep = open("Student.data", "a")
print("----------------------------------------------")
print("File Opend in Write Mode")
print("Type of filep = {}".format(type(filep)))
print("Name of the File: ", filep.name)
print("File Mode Name:", filep.mode)
print("Is File Active:", filep.closed)
print("Is File Readable:", filep.readable())
print("Is File Writable:", filep.writable())
print("----------------------------------------------")
