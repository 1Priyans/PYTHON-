# Key Word Variables Length Parameters (or) arguments
___Properties = '''When we have familiy of multiple function calls with Key Word Variable number of values / arguments 
                   then with normal python programming, we must define mutiple function defintions. This process leads 
                   to more development time. 

To overcome this process, we must use the concept of Keyword Variable length Parameters .

To Implement, Keyword Variable length Parameters concept, we must define single Function Definition and takes a formal 
Parameter preceded with a symbol called double astrisk  ( ** param) and the formal parameter with double astrisk symbol 
is called Keyword Variable length Parameters  and whose purpose is to hold / store any number of (Key,Value)  coming 
from similar function calls and whose type is <class, 'dict'>.

---------------------------------------------------------------------------------------------------
Syntax for function definition with Keyword Variables Length Parameters:
---------------------------------------------------------------------------------------------------
    def   functionname(list of formal params,  **param) :
        --------------------------------------------------
        --------------------------------------------------

Here **param is called Keyword Variable Length parameter and it can hold any number of Key word argument values (or) 
Keyword variable number of argument values and **param type is <class,'dict'>

Rule:- The **param must always written at last part of Function Heading and it must be only one (but not multiple)
---------------------------------------------------------------
Final Syntax for defining a Function
---------------------------------------------------------------
def  funcname(PosFormal parms, *Varlenparams, default params, **kwdvarlenparams):
        -------------------------------------------------
        --------------------------------------------------- '''
# Example:
# Program for demonstrating Keyword Variable Length arguments
# This Program will not execute as it is, bcoz PVM remembers Latest Function Definition only and It is a Interpeter
def data(sno, sname, sclass, shobby, sfavsub):
    print("-"*70)
    print("\tStudent Number = {}".format(sno))
    print("\tStudent Name = {}".format(sname))
    print("\tStudent Class = {}".format(sclass))
    print("\tStudent Hobby = {}".format(shobby))
    print("\tStudent Fav Subject = {}".format(sfavsub))
    print("-"*70)

def data(eno, ename, esal, eposition):
    print("-"*70)
    print("\tEmployee Number = {}".format(eno))
    print("\tEmployee Name = {}".format(ename))
    print("\tEmployee Salary = {}".format(esal))
    print("\tEmployee Position = {}".format(eposition))
    print("-"*70)

def data(tno, tname, esal):
    print("-" * 70)
    print("\tTeacher Number = {}".format(tno))
    print("\tTeacher Name = {}".format(tname))
    print("\tTeacher Salary = {}".format(esal))
    print("-" * 70)


# Main Program
data(sno=100, sname="MAVERICK", sclass="B.Tech", shobby="Cricket", sfavsub="Coding")  # Function call-1 with 5 keyword Variable length args
data(eno=101, ename="Tex", esal = 2.3, eposition="Devlopment")  # Function call-1 with 4 keyword Variable length args
data(tno=102, tname="ROSSUM", tsal=1.2)  # Function call-1 with 3 keyword Variable length args


# Program for demonstrating Keyword Variable Length arguments
# This Program will execute as it is
def data(sno, sname, sclass, shobby, sfavsub):
    print("-"*70)
    print("\tStudent Number = {}".format(sno))
    print("\tStudent Name = {}".format(sname))
    print("\tStudent Class = {}".format(sclass))
    print("\tStudent Hobby = {}".format(shobby))
    print("\tStudent Fav Subject = {}".format(sfavsub))
    print("-"*70)
# Main Program
data(sno=100, sname="MAVERICK", sclass="B.Tech", shobby="Cricket", sfavsub="Coding")  # Function call-1 with 5 keyword Variable length args

def data(eno, ename, esal, eposition):
    print("-"*70)
    print("\tEmployee Number = {}".format(eno))
    print("\tEmployee Name = {}".format(ename))
    print("\tEmployee Salary = {}".format(esal))
    print("\tEmployee Position = {}".format(eposition))
    print("-"*70)
# Main Program
data(eno=101, ename="Tex", esal = 2.3, eposition="Devlopment")  # Function call-1 with 4 keyword Variable length args

def data(tno, tname, tsal):
    print("-" * 70)
    print("\tTeacher Number = {}".format(tno))
    print("\tTeacher Name = {}".format(tname))
    print("\tTeacher Salary = {}".format(tsal))
    print("-" * 70)
# Main Program
data(tno=102, tname="ROSSUM", tsal=1.2)  # Function call-1 with 3 keyword Variable length args


# Program for demonstrating Non-Keyword Variable Length arguments
# Non-KeyWordVarLenArgs --This Program will execute as it is
def data1(sno, sname, sclass, shobby, sfavsub):
    print("-"*70)
    print("\tStudent Number = {}".format(sno))
    print("\tStudent Name = {}".format(sname))
    print("\tStudent Class = {}".format(sclass))
    print("\tStudent Hobby = {}".format(shobby))
    print("\tStudent Fav Subject = {}".format(sfavsub))
    print("-"*70)

def data2(eno, ename, esal, eposition):
    print("-"*70)
    print("\tEmployee Number = {}".format(eno))
    print("\tEmployee Name = {}".format(ename))
    print("\tEmployee Salary = {}".format(esal))
    print("\tEmployee Position = {}".format(eposition))
    print("-"*70)

def data3(tno, tname, tsal):
    print("-" * 70)
    print("\tTeacher Number = {}".format(tno))
    print("\tTeacher Name = {}".format(tname))
    print("\tTeacher Salary = {}".format(tsal))
    print("-" * 70)


# Main Program
data1(sno=100, sname="MAVERICK", sclass="B.Tech", shobby="Cricket", sfavsub="Coding")  # Function call-1 with 5 keyword Variable length args
data2(eno=101, ename="Tex", esal = 2.3, eposition="Devlopment")  # Function call-1 with 4 keyword Variable length args
data3(tno=102, tname="ROSSUM", tsal=1.2)  # Function call-1 with 3 keyword Variable length args


def data(**val):  # Here **vals are called Keyword Var length Parameter and its type is <class, dict>
    print(val, type(val))
# Main Program
data(sno=100, sname="MAVERICK", sclass="B.Tech", shobby="Cricket", sfavsub="Coding")  # Function call-1 with 5 keyword Variable length args
data(eno=101, ename="Tex", esal = 2.3, eposition="Devlopment")  # Function call-1 with 4 keyword Variable length args
data(tno=102, tname="ROSSUM", tsal=1.2)  # Function call-1 with 3 keyword Variable length args


# Program for demonstrating Keyword Variable Length arguments
def data2(**vals):  # # Here **vals are called Keyword Var length Parameter and its type is <class, dict>
    print("-" * 80)
    for key, val in vals.items():
        print("\t{} :\t{}".format(key, val))
    print("-" * 80)

    print("-" * 80)
# Main Program
data2(sno=100, sname="MAVERICK", sclass="B.Tech", shobby="Cricket", sfavsub="Coding")  # Function call-1 with 5 keyword Variable length args
data2(eno=101, ename="Tex", esal = 2.3, eposition="Devlopment")  # Function call-1 with 4 keyword Variable length args
data2(tno=102, tname="ROSSUM", tsal=1.2)  # Function call-1 with 3 keyword Variable length args

# Program for demonstrating Keyword Variable Length arguments
def findtotalmarks(sno, sname, sclass, **vals):
        print("-"*60)
        print("\tStudent Number = {}".format(sno))
        print("\tStudent Name = {}".format(sname))
        print("\tStudent Class = {}".format(sclass))
        print("-" * 60)
        totalmrks = 0
        for sn,sm in vals.items():
            print("\t{}: {}\t".format(sn, sm))
            totalmrks = totalmrks + sm
        print("Total Marks = {}".format(totalmrks))
#Main program
findtotalmarks(100, "Goku", "X", Tel=50, Hindi=60, Eng=65, Maths=66, Science=67, Social=68)
findtotalmarks(200, "Naruto", "XII", Mathematics=74, Physics=55, Chemistry=50)
findtotalmarks(300, "Vigeta", "B.Tech", cm=60, cpp=55, python=50, DBMS=50)
findtotalmarks(400, "Tex", "P.hD", RM=55)


def findtotalmarks(snumber, sname, sclass, *vals, scity="Hyd", **val):
    print("-"*80)
    print("\tStudent Number: {}".format(snumber))
    print("\tStudent Name: {}".format(sname))
    print("\tStudent Class: {}".format(sclass))
    print("\tStudent Living City: {}".format(scity))
    print("-"*80)
    print("\tSubject\t :\tMarks\t")
    print("-" * 80)
    totalmrks = 0
    for ssub, snum in val.items():
        print("\t{}\t\t\t{}\t".format(ssub, snum))
        totalmrks = totalmrks + snum
    print("Total Marks = {}".format(totalmrks))
# Main program
findtotalmarks(10, "Hulk", "X", 1.2,2.3,3.4, Tel=50,Hindi=60,Eng=65,Maths=66,Science=67,Social=68)
findtotalmarks(20, "Ironman", "XII", 9.9,9.8,9.2,9.3, Mathematics=74,Physics=55,Chemistry=50)
findtotalmarks(30, "Spiderman", "B.Tech", 3.3,3.4,3.5,4.5, city="DELHI",cm=60,cpp=55,python=50,DBMS=50)
findtotalmarks(40, "Shaktiman", "P.hD", 2.5,2.7, RM=55,city="BANG")
findtotalmarks(50, "Spoidermon", "Trainer", city="AP")


















