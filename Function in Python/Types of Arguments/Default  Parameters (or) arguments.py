# Default  Parameters (or) arguments
_Properties = '''When there is a Common Value for family of Similar Function Calls then Such type of Common Value(s) 
                 must be taken  as default parameter with common value (But not recommended to pass by using Posstional 
                 Parameters)

Syntax for Function Definition with Default Parameters
----------------------------------------------------------------------------------------
def   functionname(param1,param2,....param-n-1=Val1, Param-n=Val2):
          ------------------------------------------------------------------
	  ------------------------------------------------------------------

Here param-n-1 and param-n are called "default Parameters".
   and param1,param-2... are called "Possitional parameters".

Rule-: When we use default parameters in the function definition, They must be used as last Parameter(s) otherwise we 
       get Error( SyntaxError: non-default argument (Possitional ) follows default argument). '''

# Example:

# Program for Demonstrating Default Arguments.
def studntslst(sno, sname, smarks, cname = "USA"): # Here is cname = "USA" is Default Arguments
    print("\t{}\t\t{}\t\t\t{}\t\t\t{}".format(sno, sname, smarks, cname))

# Main Program
print("-"*100)
print("\tSNO\t\tSNAME\t\tSMARKS\t\tCNAME")
print("-"*100)
studntslst(10, "PS", 99)  # Function Call
studntslst(20, "SG", 100)  # Function Call
studntslst(30, "TK", 96)  # Function Call
studntslst(40, "PJ", 95)  # Function Call
studntslst(50, "DC", 97)  # Function Call


def dispstudinfo(sno, sname, marks, crs="PYTHON", cnt="INDIA"):
    print("\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs,cnt))


#main program
print("-------------------------------------------------------")
print("\tSNO\t\tNAME\tMARKS\t\tCOURSE\t\tCOUNTRY")
print("-------------------------------------------------------")
dispstudinfo(10, "RS", 23.45)  # Function Call
dispstudinfo(20, "DR", 33.22)  # Function Call
dispstudinfo(30, "TR", 63.22)  # Function Call
dispstudinfo(40, "MC", 23.22)  # Function Call
dispstudinfo(50, "KV", 11.11)  # Function Call
print("-------------------------------------------------------")


def dispstudinfo(sno, sname, marks, crs="PYTHON", cnt="INDIA"):
    print("\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs,cnt))


#main program
print("-------------------------------------------------------")
print("\tSNO\t\tNAME\tMARKS\t\tCOURSE\t\tCOUNTRY")
print("-------------------------------------------------------")
dispstudinfo(10, "RS", 23.45)  # Function Call
dispstudinfo(20, "DR", 33.22, cnt="USA")  # Changing country name USA
dispstudinfo(30, "TR", 63.22)  # Function Call
dispstudinfo(40, "MC", 23.22, crs="JAVA")  # Function Call Changing course name JAVA
dispstudinfo(50, "KV", 11.11)  # Function Call
print("-------------------------------------------------------")



def dispstudinfo(sno, sname, marks, crs="PYTHON", cnt="INDIA"):
    print("\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs,cnt))

def dispstudinfo1(sno, sname, marks, crs="JAVA", cnt="USA"):
    print("\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs,cnt))


#main program
print("-------------------------------------------------------")
print("\tSNO\t\tNAME\tMARKS\t\tCOURSE\t\tCOUNTRY")
print("-------------------------------------------------------")
dispstudinfo(10, "RS", 23.45)  # Function Call
dispstudinfo(20, "DR", 33.22, cnt="USA")  # Changing country name USA
dispstudinfo(30, "TR", 63.22)  # Function Call
dispstudinfo(40, "MC", 23.22,)  # Function Call Changing course name JAVA
dispstudinfo(50, "KV", 11.11)  # Function Call
print("-------------------------------------------------------")
print("="*70)
print("-------------------------------------------------------")
print("\tSNO\t\tNAME\tMARKS\t\tCOURSE\t\tCOUNTRY")
print("-------------------------------------------------------")
dispstudinfo1(101, "RSS", 2.45)  # Function Call
dispstudinfo1(202, "DRS", 33.2)  # Changing country name USA
dispstudinfo1(303, "TSR", 63.2)  # Function Call
dispstudinfo1(404, "MSC", 23.2, crs="C++")  # Function Call Changing course name JAVA
dispstudinfo1(505, "KVR", 11.1)  # Function Call
print("-------------------------------------------------------")


# Program for calculating Area and Perimiter of Circle
def area(r, pi = 3.14):
    ar = pi * r ** 2
    print("Area of Circle = {}".format(ar))

def perimtr(r, pi = 3.14):
    pmtr = 2 * pi * r
    print("Perimeter of Circle = {}".format(pmtr))

print("-"*80)
r = int(input("Enter the Radius of given Circle: "))
area(r)
print("-"*80)
r = int(input("Enter the Radius of given Circle: "))
perimtr(r)
print("-"*80)




