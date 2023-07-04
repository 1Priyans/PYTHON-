from Addition import AddOp
from Pdc import PythonValueError
try:
    x, y = int(input("Enter First Value: ")), int(input("Enter Second Value: "))
    res = AddOp(x, y)
except PythonValueError:
    print("Don't Enter Alphanumerics, str, and symbols")
else:
    print("Addition of ({} + {}) = {}".format(x, y, x + y))

