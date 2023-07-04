# Main Program
from MulTable import Table
from MultableExcept import NegativeNumError, ZeroError
n = input("Enter a Number for Generating Mul Table: ")
try:
    Table(n)
except (NegativeNumError):
    print("Don't Enter -ve Number for Mul Table")
except (ZeroError):
    print("Don't Enter Zero for Mul Table")
except (ValueError):
    print("Don't Enter Alphanum, str and symbols for Mul Table")
except:
    print("Some Thing Went Wrong")
