from Pdc import PythonValueError
def AddOp(a, b):
    x, y = int(a), int(b)  # This Statement may Implicitly raise ValueError if num contains alnums, pure str and Symbols
    return x + y


