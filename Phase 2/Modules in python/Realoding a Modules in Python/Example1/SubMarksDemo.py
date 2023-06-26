# SubMarks.py-----> File Name and Module Name
import importlib
import time
import SubMarks
def displ(d):
    print("-" * 60)
    print("\tSubject\t\tMarks\t")
    print("-" * 60)
    for sn,sm in d.items():
        print("\t{} \t\t {}\t".format(sn,sm))
    else:
        print("-" * 60)

# Main Program
d = SubMarks.MarksInfo()
displ(d)
print("I am going to Sleep for 15 seconds")
time.sleep(15)
print("-" * 60)
print("I am  Coming out of Sleep after 15 seconds")
importlib.reload(SubMarks)  # relodaing previously imported module
d = SubMarks.MarksInfo()  # obtaining changed / new values of previously  imported	module
displ(d)
d = SubMarks.MarksInfo()
displ(d)
print("I am going to Sleep for 15 seconds")
time.sleep(15)
print("-" * 60)
print("I am  Coming out of Sleep after 15 seconds")
importlib.reload(SubMarks)  # relodaing previously imported module
d = SubMarks.MarksInfo()  # obtaining changed / new values of previously  imported	module
displ(d)