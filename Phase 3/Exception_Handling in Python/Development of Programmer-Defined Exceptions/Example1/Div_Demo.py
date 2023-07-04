from Division import divop
from Pdc import PythonZeroDivError
a, b = int(input("Enter First Value: ")), int(input("Enter Second Value: "))
try:
    res = divop(a,b)  # Function Call---> Gives Result OR Exception
except PythonZeroDivError:
    print("Don't Enter Zero in Denominator")
else:
    print("Division of ({}/{}) = {}".format(a, b, res))