# Program for Demonstrating Writing the data to the file
stn = "Maverick and Tex"
strno = 21
stmrks = 86
with open("stud.info","w") as stinfo:
    stinfo.write(stn +"\t")
    stinfo.write(str(strno)+"\t")
    stinfo.write(str(stmrks)+"\t")

