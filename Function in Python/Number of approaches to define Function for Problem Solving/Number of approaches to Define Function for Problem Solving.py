# Number of approaches to Define Function for Problem Solving
__Properties = '''To Define any Function in Python, We have 4 approaches. They are

Approach-1
-----------
Function for defining addition of two Numbers
INPUT: Taking INPUT from Function Call (main program )
PROCESSING:Doing the Process in Function Body
RESULT/OUTPUT:Giving the result to Function Call

def addop(a,b):  # here a and b are called formal params
    print("-----------------------------")
    print("I am from Function Definition")
    c=a+b # Here c is called Local variable--Processing
    return c # Returing the Result to main program
#Main Program
#Accepting the Input from Main program
a = float(input("Enter First Value:"))
b = float(input("Enter Second Value:"))
c = addop(a,b) # Function call
print("sum({},{})={}".format(a,b,c)) 


Approach-2
-----------
Function for defining addition of two Numbers
INPUT: Taking INPUT in Function Body
PROCESSING: Doing the Process in Function Body
RESULT/OUTPUT:Display the result / output in Function Body

def addop():
    #Taking INPUT in Function Body
    k=float(input("Enter First Value:"))
    v=float(input("Enter Second Value:"))
    #Doing the Process in Function Body
    r=k+v
    #Display the result / output in Function Body
    print("sum({},{})={}".format(k,v,r))

main program
addop() # Function call


Approach-3
-----------
Function for defining addition of two Numbers
INPUT: Taking INPUT from Function Call (main program )
PROCESSING:Doing the Process in Function Body
RESULT/OUTPUT:Display the result / output in Function Body

def addop(a,b):
    c=a+b
    print("sum({},{})={}".format(a,b,c))
#main program
x=float(input("Enter First Value:"))
y=float(input("Enter Second Value:"))
addop(x,y) # Function call


Approach-4
------------
Function for defining addition of two Numbers
INPUT: Taking INPUT in Function Body
PROCESSING: Doing the Process in Function Body
RESULT/OUTPUT: Giving the result to Function Call

def addop():
    # Taking INPUT in Function Body
    k = float(input("Enter First Value:"))
    v = float(input("Enter Second Value:"))
    # Doing the Process in Function Body
    r = k + v
    #Give the result back to function call
    return k,v,r # here return can  return Multiple Values

#main program
x,y,res=addop() # Function call with Multi Line assigment
print("sum({},{})={}".format(x,y,res))
print("==============OR===============")
res=addop() # Function call with single line assigment
#Here res is an object of type tuple
print("sum({},{})={}".format(res[0],res[1],res[2]))
print("sum({},{})={}".format(res[-3],res[-2],res[-1])) '''



















