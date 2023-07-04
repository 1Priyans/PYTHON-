from Fact_Cal import Fact
from FactExcept import NegNumError
def factorial():
    n = input("Enter a Number for Cal Factorial: ")
    try:
        Fact(n)
    except ValueError:
        print("Can't Cal Factorial for Alphanums, str and symbols")
    except NegNumError:
        print("Don't Enter -Ve num for cal Factorial")
    except:
        print("Something Went Wrong")

# MAin Program
factorial()