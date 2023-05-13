# We are perfom two types of operations 1.indexing  2.Slicing
# In indexing : The Process of Obtaining a single Value from str object is called Indexing.
# Index can be either +ve or -ve
a ="Priyansh Soni"
print(a[0])
print(a[8]) #Getting Output as space

_Information = '''Guido van Rossum
... HNO:3-4,Hill Side
... Python Software Foundation
... Nether Lands-56'''
print(_Information[3])
print(_Information[-1])

#In Slicing : The process of obtaing Range of Chars/Sub string from given main string data is called slicing
__informatin = '''Slicing operation contains 5 syntaxes. They are:
1. strobj[begin:End]
2. strobj[Begin:]
3. strobj[:End]
4. strobj[:] '''
#Syntax1. strobj[Begin:End]
#This Syntax Gives Range of Chars from PosBegin to NegEnd-1 Index Provided PosBeg>NegEnd Index Otherwise 
#we never get  any result (space)
a = "PYTHON"
print(a[1:3])

#Syntax2. strobj[Begin:]
# In This Syntax we are specifying BEGIN Index and Not Specifying END Index.
# If we don't specify END Index then PVM Takes upto Last Character.
# 				(OR)
# If we don't specify END Index then PVM Takes END Index as  len(strobj)
a = "PYTHON"
print(a[1:])
print(len(a))
print(a[-4:])
print(a[-1:])
print(a[-8:])

#Syntax3. strobj[:End]
# In This Syntax we are specifying END Index and Not Specifying BEGIN Index.
# If we don't specify BEGIN  Index then PVM TakesFrom First Character onwards.
# 				(OR)
# If we don't specify BEGIN Index then PVM Takes BEGIN  Index as 0 OR -len(strobj).
a = "PYTHON"
print(a[:1])
print(len(a))
print(a[:-4])
print(a[:-1])
print(a[:-8])

#Syntax4. strobj [ : ]
# In This Syntax we are not specifyingBoth BEGIN Index and  END Index.
# If we don't specify Begin Index and END Index then PVM Takes First Character  upto Last Character.
# 				(OR)
# If we don't specify Begin Index and  END Index then PVM Takes Begin Index as 0 or -len(strobj) and  
# END Index as  len(strobj) or -1
a = "PYTHON"
# print[-len(a):]
# print[:len(a)]
#NOTE: In Syntax-1,Syntax-2,Syntax-3, and Syntax-4, we are getting the data in FORWARD DIRECTION
#with Step 1 (letter by letter--sequence)

#Syntax5. Strobj[Begin:End:Step]
#Rule-1:  Here BEGIN,END and STEP can either +VE or -VE 
#Rule-2: If STEP Value is +VE then PVM get the Chars from BEGIN Index to END-1 Index in FORWARD 
#Direction provided BEGIN<END otherwise never get any Result
a = "PYTHON"
print(a[0:6:2])
print(a[5:3:2])
print(a[3:4:4])
print(a[1:5:4])
print(a[1:5:4])
print(a[-1:-5:4])

#Rule-3: If STEP Value is -VE then PVM gets the Chars from BEGIN Index to END+1 Index in BACKWARD 
#Direction Provided BEGIN>END otherwise never get any Result
a = "PYTHON"
print(a[5:1:-1])
print(a[5:1:-1])
print(a[::-1])
print(a[1:6:-1])
print(a[5:0:-2])
print(a[4:0:-2])
print(a[4::-2])
print(a[0:6:2])
print(a[0:6:2][::-1]) # PTO then [::-1]) give its reversal

print(a[-6:-1:-1])
print(a[-1:-6:-1])
print(a[-1:-6:-2])
print(a[-1::-3])
print(a[::-3])
print(a[::-2])
print((a[::-2])[::-1])
print(a[-1:-6-3])

#Rule-4: When we extract the chars in FORWARD Direction, If the END Index is 0 then we never 
# get any result(space)
print(a[:0:2])
print(a[:0:3])
print(a[:0:3])
print(a[:0:2])

#Rule-5: When we extract the chars in BACKWARD Direction, If the END Index is -1 then we never get 
# any result(space)
print(a[:-2:2])
print(a[:-4:-3])
print(a[:-5:-3])
print(a[:-3:-2])

#Special points
print(a[:100])
print(a[-100:-1])
print(a[-100:])




