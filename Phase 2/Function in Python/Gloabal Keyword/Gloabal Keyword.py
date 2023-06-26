# Global key word
__Properties = """When we want MODIFY the GLOBAL VARIABLE values in side of function defintion then global variable names must be preceded with 'global' keyword otherwise we get 
  "UnboundLocalError: local variable names referenced before assignment"
------------
Syntax:
-----------
    var1=val1
    var2=val2
    var-n=val-n    #  var1,var2...var-n are called global variable names.
    ------------------
    def   fun1():
        ------------------------
        global var1,var2...var-n
        # Modify var1,var2....var-n
        --------------------------
    def   fun2():
           ------------------------
            global var1,var2...var-n
         # Modify var1,var2....var-n
	       -------------------------- """

# Example:
# Program for demonstrating global keyword
def increment():
    global a
    a = a + 1  # "UnboundLocalError: local variable names referenced before assignment" Without using global keyword

def update():
    global a
    a = a * 2

# Main Program
a = 10  # Here 'a' is a global variable
print("Global Value Before Increment a is {}".format(a))  # Global Value Before Increment a is 10
increment()
print("Global Value After Increment a is {}".format(a))  # Global Value Before Increment a is 11
update()
print("Global Value After Updation a is {}".format(a))  # Global Value Before Increment a is 22


# Program for demonstrating global keyword
def Addition():
    global a, b
    a = a + 1
    b = b + 1

def Multiplication():
    global a, b
    a = a * 3
    b = b * 4

# Main Program
a, b = 1, 2
print("Before Addition Gloabal Values a = {}, b = {}".format(a, b))  # Before Addition Gloabal Values a = 1, b = 2
Addition()
print("After Addition Gloabal Values a = {}, b = {}".format(a, b))  # After Addition Gloabal Values a = 2, b = 3
Multiplication()
print("Before Addition Gloabal Values a = {}, b = {}".format(a, b))  # Before Addition Gloabal Values a = 6, b = 12



















