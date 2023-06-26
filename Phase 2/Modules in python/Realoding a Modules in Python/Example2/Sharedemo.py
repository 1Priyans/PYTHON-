# Shares.py----> File Name and Module Name
import time
import Shares
import importlib
def displ(d):
    print("-" * 70)
    print("\tShare's Name\t\tRate")
    print("-" * 70)
    for sn,sr in d.items():
        print("\t{}\t\t\t\t\t{}\t".format(sn,sr))
# Main Program
d = Shares.Sharesinfo()
displ(d)
time.sleep(15)
importlib.reload(Shares)
d = Shares.Sharesinfo()  # obtaining changed / new values of previously  imported	module
displ(d)


