# Variables Length Parameters (or) arguments
__Properties = '''When we have familiy of multiple function calls with Variable number of values / arguments then 
with normal python programming, we must define mutiple function defintions. This process leads to more
development time. 

To overcome this process, we must use the concept of Variable length Parameters .

To Impelement, Variable length Parameters concept, we must define single Function Definition and takes a formal Parameter 
preceded with a symbol called astrisk ( * param) and the formal parameter with astrisk symbol is called Variable length 
Parameters  and whose purpose is to hold / store any number of values coming from similar function calls and whose type 
is <class, 'tuple'>.

---------------------------------------------------------------------------------------------------
Syntax for function definition with Variables Length Parameters:
--------------------------------------------------------------------------------------------------
	def   functionname(list of formal params,  *param1,param2=value) :
	        --------------------------------------------------
		--------------------------------------------------

Here *param1 is called Variable Length parameter and it can hold any number of argument values (or) variable number of 
argument values and *param1 type is <class,'tuple'>

Rule:- The *param1 must always written at last part of Function Heading and it must be only one (but not multiple)

Rule:- When we use Variable length and default parameters  in function Heading, we use default parameter as last and 
before we use variable length parameter and in function calls, we should not use default parameter as Key word argument 
bcoz Variable number of values are treated as Posstional Argument Value(s) .'''

# Example:

# Program for demonstrating variable Length arguments
# This Program will not execute as it as bcoz PVM is remebers Latest Function definition only bcoz PVM performs Interpretation Process.
def  disp(a,b,c,d,e): # Function Def-1
	print(a,b,c,d,e)

def disp(a,b,c,d): # Function Def-2
	print(a,b,c,d)

def disp(a,b,c): # Function Def-3
	print(a,b,c)

def disp(a,b): # Function Def-4
	print(a,b)

def disp(a): # Function Def-5
	print(a)

# Main Program
disp(10,20,30,40,50) # Function Call-1
disp(10,20,30,40) # Function Call-2
disp(10,20,30) # Function Call-3
disp(10,20) # Function Call-4
disp(10) # Function Call-5

# Program for demonstrating variable Length arguments
# This Program will  execute as it as
def diplay(a, b, c, d, e):
    print(a, b, c, d, e)

diplay(10, 20, 30, 40, 50)

def diplay(a, b, c, d):
    print(a, b, c, d)

diplay(10, 20, 30, 40)

def diplay(a, b, c):
    print(a, b, c)

diplay(10, 20, 30)

def diplay(a, b):
    print(a, b)

diplay(10, 20)

def diplay(a):
    print(a)

diplay(10)


# Program for demonstrating variable Length arguments
def disp(*a): # here *a is called variable Length Param and whose type is <class, tuple>
    print(a, type(a))
# Main Program
disp(10,20,30,40,50) # Function Call-1
disp(10,20,30,40) # Function Call-2
disp(10,20,30) # Function Call-3
disp(10,20) # Function Call-4
disp(10) # Function Call-5

# Program for demonstrating variable Length arguments
def disp(*a):  # here *a is called variable Length Param and whose type is <class, tuple>
    print("-"*100)
    print("Number of Values = {}".format(len(a)))
    print("-"*100)
    for val in a:
        print(val,type(val))
    print("-"*100)
# Main Program
disp(10,20,30,40,50) # Function Call-1
disp(10,20,30,40) # Function Call-2
disp(10,20,30) # Function Call-3
disp(10,20) # Function Call-4
disp(10) # Function Call-5


# Program for demonstrating variable Length arguments
def display(sno, subname, *val):  # here *vals is called variable Length Param and whose type is <class, tuple>
    print("-"*90)
    print("Student Number = {}".format(sno))
    print("Subject Name = {}".format(subname))
    print("-"*90)
    s = 0
    for i in val:
        print("\t{}".format(i))
        s = s + i
    print("-" * 90)
    print("\tSum = {}".format(s))
    print("-" * 90)
# Main Program
display(100, "PYTHON", 10, 20, 30, 40, 50)  # Function Call-1 with 5 args
display(200, "JAVA", 10, 20, 30, 40)  # Function Call-2 with 4 args
display(300, "C++", 10, 20, 30)  # Function Call-3 with 3 args
display(400, "C", 10, 20)  # Function Call-4 with 2 args
display(500, "C#.net", 10)  # Function Call-5 with 1 args
display(600, "JAVA Script")  # Function Call-6 with no args


# Program for demonstrating variable Length arguments
def disp(pno, pname, *vals, pgun = "AK-47"):
    print("-"*70)
    print("Player Number = {}".format(pno))
    print("Player Name = {}".format(pname))
    print("Player Gun = {}".format(pgun))
    print("-" * 70)
    s = 0
    for val in vals:
        print("\t{}".format(val))
        s = s + val
    print("-" * 70)
    print("\tSum = {}".format(s))
    print("-" * 70)
# Main Program
disp(1, "Maverick", 10, 20, 30, 40, 50)  # Function Call-1 with 5 args
disp(2, "Maniac", 10, 20, 30, 40)  # Function Call-2 with 4 args
disp(3, "Rabel", 10, 20, 30)  # Function Call-3 with 3 args
disp(4, "Vandal", 10, 20)  # Function Call-4 with 2 args
disp(5, "Tex", 10)  # Function Call-5 with 1 args


# Program for demonstrating non-variable Length arguments
def  disp1(a, b, c, d, e): # Function Def-1
    print(a, b, c, d, e)

def disp2(a, b, c, d): # Function Def-2
    print(a, b, c, d)

def disp3(a, b, c): # Function Def-3
    print(a, b, c)

def disp4(a, b): # Function Def-4
    print(a, b)

def disp5(a): # Function Def-5
    print(a)

#main program
disp1(10,20,30,40,50) # Function Call-1
disp2(10,20,30,40)  # Function Call-2
disp3(10,20,30)  # Function Call-3
disp4(10,20)  # Function Call-4
disp5(10)  # Function Call-5





























