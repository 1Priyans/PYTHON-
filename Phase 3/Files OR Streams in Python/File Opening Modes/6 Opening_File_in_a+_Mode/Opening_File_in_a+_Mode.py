_ = """
6) a+
------------------------------------------------------------------------------------------------------------------------------------
=>This Mode is used for Creating a File and Opening the File in Write Mode.
=>In Otherwords, If we Open NEW FILE in "a+" Mode Then That File created and Opened in write Mode and we 
    can write the data. If we Open EXISTING FILE in "a+" Mode Then That File  Opened in write Mode and New Data 
    APPENDED at the end of Existing data and Later we can also Perform READ Operation."""
# Example:
with open("Student1.data", "a+") as fp:
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