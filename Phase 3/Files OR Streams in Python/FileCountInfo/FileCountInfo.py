# Program for Finding Number of Lines,Words and Characters of any File
filename = input("Enter Any File Name: ")
try:
    with open(filename, "r") as fp:
        filedata = fp.readlines()
        nl = 0
        nw = 0
        nc = 0
        for lines in filedata:
            print(lines, end='')
            nl = nl + 1
            nw = nw + len(lines.split())
            nc= nc + len(lines)
        else:
            print("-" * 80)
            print("Number of Lines = {}".format(nl))
            print("Number of Word = {}".format(nw))
            print("Number of Characters = {}".format(nc))
            print("-" * 80)
except FileNotFoundError:
    print("File Does Not Exist")

