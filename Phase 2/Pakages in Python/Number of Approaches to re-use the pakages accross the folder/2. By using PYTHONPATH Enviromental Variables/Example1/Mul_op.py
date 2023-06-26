# Mul_op.py---> File Name and Module Name
num = int(input(("Enter a Number you want to Generate Multiplication Table: ")))
def MulTable():
    print("Multiplication Table of {}".format(num))
    for i in range(1, 11):
        print("{} * {} = {}".format(num,i,num*i))
