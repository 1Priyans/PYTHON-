# Keyword Arguments or Parameters
___Properties = '''In some of the circumstances, we know the function name and formal parameter names and we don't know
                   the order of formal Parameter names and to pass the data / values accurately we must use the concept 
                   of Keyword Parameters (or) arguments.

The implementation of Keyword Parameters (or) arguments says that all the formal parameter names used as arguments in 
Function call(s) as keys.

Syntax for function definition:-
-------------------------------------------------
def    functionname(param1,param2...param-n):
         ---------------------------------------------
        ---------------------------------------------

Syntax for function call:-
-------------------------------------------------
    functionname(param-n=val-n,param1=val1,param-n-1=val-n-1,.........)

Here param-n=val-n,param1=val1,param-n-1=val-n-1,...... are called Keywords arguments

When we specify Keyword arguments before Possitional Arguments in Function Calls(s) then we get SyntaxError: positional
 argument follows keyword argument'''

# Example:
# Program for Demonstrating Keyword Arguments
def  disp(a,b,c,d):
    print("\t{}\t{}\t{}\t{}".format(a,b,c,d))

#main program
print("-------------------------------------------------------")
print("\tA\tB\tC\tD")
print("-------------------------------------------------------")
disp(10,20,30,40)  # Function Call with Possitional Args
disp(d=40, a=10, c=30, b=20)  # Function Call with Keyword Args
disp(b=20, c=30, d=40, a=10)  # Function Call with Keyword Args
disp(10, 20, d=40, c=30)  # Function Call with Positional Args and Keyword Args
# disp(d=40,c=30,10,20)----SyntaxError: positional argument follows keyword argument
disp(d=40, c=30, a=10, b=20)  # Function Call with Keyword Args
print("-------------------------------------------------------")


def disp(a,b,c,d,cnt="INDIA"):
    print("\t{}\t{}\t{}\t{}\t{}".format(a,b,c,d,cnt))

#main program
print("-------------------------------------------------------")
print("\tA\tB\tC\tD\tCOUNTRY")
print("-------------------------------------------------------")
disp(10, 20, 30, 40) # Function Call with Possitional Args
disp(d=40, a=10, c=30, b=20)  # Function Call with Keyword Args
disp(b=20, c=30, d=40,a=10)  # Function Call with Keyword Args
disp(10, 20, d=40, c=30)  # Function Call with Possitional Args and Keyword Args
#disp(d=40, c=30, 10, 20)----SyntaxError: positional argument follows keyword argument
disp(d=40, c=30, a=10, b=20)  # Function Call with Keyword Args
disp(d=40, cnt="USA", a=10, c=30, b=20)  # Function Call with Keyword Args along with default values
print("-------------------------------------------------------")








