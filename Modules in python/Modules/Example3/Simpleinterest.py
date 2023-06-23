# Simpleinterest.py----> File Name and Module Name
def simpleinst(p,t,r):
    p, t, r = float(input("Enter Principle Amount: ")),float(input("Enter Time: ")),float(input("Enter Rate og Interest: "))
    si = (p * t * r)/100
    print("Prnciple Amount = {}".format(p)), print("Time = {}".format(t)), print("Rate of Interest = {}".format(r))
    print("-"*70)
    print("Simple Interest = {}".format(si))
    print("-" * 70)
    totlam = p + si
    print("-" * 70)
    print("Total Amount of Pay = {}".format(totlam))
    print("-" * 70)

