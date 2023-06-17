# Global and Local variables and Globals()
__Properties = '''When we come acrosss same global Variable names and Local Variable Names in same function definition then PVM gives preference for local variables but not for 
  global variables.

In this context, to extract / retrieve the values of global variables names along with local variables, we must use globals() and it returns an object of 
  <class,'dict'> and this dict object stores all global variable Names as Keys and global variable values as values of value.

Syntax:-
        var1=val1
        var2=val2
        --------------
        var-n=val-n  # var1, var2...var-n are called global Variables
        def    functionname():
               ------------------------
               var1=val11
               var2=val22
               -----------------
               var-n=val-nn  #  var1, var2...var-n are called local Variables
               # Extarct  the global variables values
               dictobj=globals()
               ------------------------
               globalval1=dictobj['var1']  #  or  dictobj.get("var1") or globals()['var1'] or global().get('var1')
               globalval2=dictobj['var2']  # or dictobj.get("var2") or globals()['var2']
               -----------------------------------------------------
               -----------------------------------------------------
=================================================================='''
# Program for demonstrating globals()
a = 10
b = 20
c = 30
d = 40
e = 50  # Here a, b, c, e are Global Variables
def Addiition():
    p = 10
    q = 20
    r = 30
    s = 40  # Here p, q, r, s are Local Variables
    adtion = a + b + c + d + e + p + q + r + s
    print("\tAddition of Global and Local variables = {}".format(adtion))  # Addition of Global and Local variables = 250
# Main Program
# Addiition()


# Program for demonstrating globals()
a = 10
b = 20
c = 30
d = 40
e = 50  # Here a, b, c, e are Global Variables
def Addiition():
    a = 100
    b = 200
    c = 300
    d = 400
    e = 500  # Here p, q, r, s are Local Variables
    adtion = a + b + c + d + e + a + b + c + d + e
    print("\tAddition of Global and Local variables = {}".format(adtion))  # Addition of Global and Local variables = 3000
# Here we can see that both(Global & Local Variables) having same values so PVM gives first Preference to Local Variables
# i.e. here a = 100, b = 200, c = 300, d = 400, e = 500
# Main Program
Addiition()


# Program for demonstrating globals()
a = 10
b = 20
c = 30
d = 40
e = 50  # Here a, b, c, e are Global Variables
def Addiition():
    a = 100
    b = 200
    c = 300
    d = 400
    e = 500  # Here p, q, r, s are Local Variables
    adtion = a + b + c + d + e + globals()['a'] + globals().get('b') + globals()['c'] + globals()['d'] + globals()['e']
    print("\tAddition of Global and Local variables = {}".format(adtion))  # Addition of Global and Local variables = 1650
# Main Program
Addiition()


# Program for demonstrating globals()
a = 10
b = 20
c = 30
d = 40
e = 50  # Here a, b, c, e are Global Variables
def Addiition():
    f = globals()
    a = 100
    b = 200
    c = 300
    d = 400
    e = 500  # Here p, q, r, s are Local Variables
    adtion = a + b + c + d + e + globals()['a'] + globals().get('b') + globals()['c'] + f['d'] + f.get('e')
    print("\tAddition of Global and Local variables = {}".format(adtion))  # Addition of Global and Local variables = 1650
# Main Program
Addiition()


# Program for demonstrating globals()
a = 10
b = 20
c = 30
d = 40
e = 50  # Here a, b, c, e are Global Variables
def Operation():
    f = globals()
    print("-" * 80)
    print("Programmers Invisible Variable Names: ")
    print("-" * 80)
    for k, v in f.items():
        print("\t{}---->{}\t".format(k, v))
    print("-" * 80)
    print("Programmer Global Variable Names--> Way1:")
    print("Val of a = {}".format(globals()['a']))
    print("Val of b = {}".format(globals()['b']))
    print("Val of c = {}".format(globals()['c']))
    print("Val of d = {}".format(globals()['d']))
    print("Val of e = {}".format(globals()['e']))
    print("-" * 80)

    print("-" * 80)
    print("Programmer Global Variable Names--> Way2:")
    print("Val of a = {}".format(globals().get('a')))
    print("Val of b = {}".format(globals().get('b')))
    print("Val of c = {}".format(globals().get('c')))
    print("Val of d = {}".format(globals().get('d')))
    print("Val of e = {}".format(globals().get('e')))
    print("-" * 80)

    print("-" * 80)
    print("Programmer Global Variable Names--> Way3:")
    print("Val of a = {}".format(f.get('a')))
    print("Val of b = {}".format(f.get('b')))
    print("Val of c = {}".format(f.get('c')))
    print("Val of d = {}".format(f.get('d')))
    print("Val of e = {}".format(f.get('e')))
    print("-" * 80)

    print("-" * 80)
    print("Programmer Global Variable Names--> Way4:")
    print("Val of a = {}".format(f['a']))
    print("Val of b = {}".format(f['b']))
    print("Val of c = {}".format(f['c']))
    print("Val of d = {}".format(f['d']))
    print("Val of e = {}".format(f['e']))
    print("-" * 80)

# Main Program
Operation()














