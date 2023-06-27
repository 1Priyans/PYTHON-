# Program for finding index of a letter in str data enter by the user
def index():
    s = input("Enter a Word/Line of Text: ")
    letter = input("Enter the Letter for find its Indices: ")
    for indexval in range(0, len(s)):
        if(s[indexval] == letter):
            print("'{}' Present in {} index".format(letter,indexval))

# Main Program
index()