_ = '''
1) r      
------------------------------------------------------------------------------------------------------------------------------------
=>This Mode is used for Opening the File in Read Mode.
=>"r" is Default File Mode.
=>If we Open the file Name in "r" Mode and If the file name does not exist then we get FileNotFoundError.'''
# Example:
# Program Opening the file in Read Mode
try:
    filep = open("../2 Opening_File_in_w_Mode/Student.data")
except FileNotFoundError:
    print("File Does not Exist")
else:
    print("----------------------------------------------")
    print("File Opened in Read Mode")
    print("Type of filep = {}".format(type(filep)))
    print("Name of the File: ", filep.name)
    print("File Mode Name:", filep.mode)
    print("Is File Active:", filep.closed)
    print("Is File Readable:", filep.readable())
    print("Is File Writable:", filep.writable())
    print("----------------------------------------------")
finally:
    print("I am From Finally Block")
    filep.close()
    print("Is File Active:", filep.closed)

