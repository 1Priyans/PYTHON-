from Pdc import PythonZeroDivError

def divop(a,b):
    if b == 0:
        raise PythonZeroDivError
    else:
        return a/b



