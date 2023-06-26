# Local variables and Global Variables
_Properties = '''Local Variables
-------------------
The Variables used inside of Function Body are called Local Variables.

The Purpose of Local Variables is that "To Store the Temporary results".

Local Variables Can be accessed inside of Corresponding Function Body But Not possible to access in other 
    Part of the program.
------------
Syntax:
-----------
def functionname(list of formal Params if any):
    -------------------------------
    var1=val1
    var2=Val2
    ------------
    ar-n=val-n
    ---------------			
here var1,var2..var-n are called Local Variables.

--------------------
Global Variables
--------------------
Global variables are those which are common  values for different function calls.

In Other words, if the Value is common for all Different Function Calls then such type 
     of values must be taken as Global Variables.

To access the values of Global Variables then They Must be defined Before Function 
     Calls only otherwise we get NameError.

Syntax:            var1=val1
            var2=val2
            -------------
            var-n=val-n

            def   fun1():
                -----------
                -----------
            def   fun2():
                -----------
                -----------

            def   fun-n():
                -----------
                -----------

Here Var1, Var2..var-n are called Global variables and we can access those values inside of fun1(), fun2()....fun-n().'''
# Example
# Program for demonstrating Local and Global Variables
lang2 = "Python"  # Here lang is Global Variable
def diplinfomtion():
    fun1 = "AI"  # Here fun1 is Local Variable
    print("To Develope {} Based Aplication, we must use {} Programming language".format(fun1, lang))
def diplinfomtion1():
    fun2 = "ML"  # Here fun2 is Local Variable
    print("To Develope {} Based Aplication, we must use {} Programming language".format(fun2, lang))
# Main Program
diplinfomtion()
diplinfomtion1()


# Program for demonstrating Local and Global Variables
def diplinfomtion():
    fun1 = "AI"  # Here fun1 is Local Variable
    print("To Develope {} Based Aplication, we must use {} Programming language".format(fun1, lang))

lang1 = "Python"  # Here lang is Global Variable

def diplinfomtion1():
    fun2 = "ML"  # Here fun2 is Local Variable
    print("To Develope {} Based Aplication, we must use {} Programming language".format(fun2, lang))
# Main Program
diplinfomtion()
diplinfomtion1()


# Program for demonstrating Local and Global Variables
def diplinfomtion():
    fun1 = "AI"  # Here fun1 is Local Variable
    print("To Develope {} Based Aplication, we must use {} Programming language".format(fun1, lang))
def diplinfomtion1():
    fun2 = "ML"  # Here fun2 is Local Variable
    print("To Develope {} Based Aplication, we must use {} Programming language".format(fun2, lang))
# Main Program
lang3 = "Python"  # Here lang is Global Variable
diplinfomtion()
diplinfomtion1()

# Program for demonstrating Local and Global Variables
def diplinfomtion():
    fun1 = "AI"  # Here fun1 is Local Variable
    print("To Develope {} Based Aplication, we must use {} Programming language".format(fun1, lang))

def diplinfomtion1():
    fun2 = "ML"  # Here fun2 is Local Variable
    print("To Develope {} Based Aplication, we must use {} Programming language".format(fun2, lang))
# Main Program
diplinfomtion()
lang4 = "Python"  # We can't access the value of 'lang' in learnAI() bcoz 'lang' defined after learnAI()
diplinfomtion1()












