# Positional Arguments
__Properties = '''The Concept of Possitional Parameters (or) arguments says that "The Number of Arguments of Function 
                  Call must be equal to the number of formal parameters in Function Heading".

This Parameter mechanism also recommends to follow Order and Meaning of Parameters for Higher accuracy.

To pass the Specific Data from Function Call to Function Definition then we must take Possitional Argument Mechanism. 

The default Parameter Passing Mechanism is Possitional  Arguments (or) Parameters. 
-----------------------------------------------
Syntax for Function Definition :
-----------------------------------------------
	def    functionname(param1,param2.....param-n):
		-------------------------------------------------
		-------------------------------------------------

-----------------------------------------------
Syntax for Function Call:
-----------------------------------------------
		functionname(arg1,arg2....arg-n)

Here the values of arg1,arg2...arg-n are passing to param-1,param-2..param-n respectively.

PVM gives First Priority to Positional Arguments.'''

# Example:

# Program for Demonstrating Possitional Arguments
def studntslst(sno, sname, smarks):
    print("\t{}\t\t{}\t\t{}".format(sno, sname, smarks))

# Main Program
print("-"*100)
print("\tSNO\t\tSNAME\tSMARKS")
print("-"*100)
studntslst(10, "PS", 99) # Function Call
studntslst(20, "SG", 100) # Function Call
studntslst(30, "TK", 96) # Function Call
studntslst(40, "PJ", 95) # Function Call
studntslst(50, "DC", 97) # Function Call

def  dispstudinfo(sno,sname,marks,crs):
    print("\t{}\t\t{}\t\t\t{}\t\t{}".format(sno,sname,marks,crs))


#main program
print("-------------------------------------------------------")
print("\tSNO\t\tNAME\t\tMARKS\t\tCOURSE")
print("-------------------------------------------------------")
dispstudinfo(10,"RS",23.45,"PYTHON") # Function Call
dispstudinfo(20,"DR",33.22,"PYTHON") # Function Call
dispstudinfo(30,"TR",63.22,"PYTHON") # Function Call
dispstudinfo(40,"MC",23.22,"PYTHON") # Function Call
dispstudinfo(50,"KV",11.11,"PYTHON") # Function Call
print("-------------------------------------------------------")




















