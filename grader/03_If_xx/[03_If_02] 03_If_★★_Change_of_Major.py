id1,gpax1,cp1,cal11,cal21 = input().split()
gpax1 = float(gpax1)
id2,gpax2,cp2,cal12,cal22 = input().split()
gpax2 = float(gpax2)

aboveOrEqualC = 'ABC'
if( (cp1 != 'A' or cal11 not in aboveOrEqualC or cal21 not in aboveOrEqualC) and (cp2 != 'A' or cal12 not in aboveOrEqualC or cal22 not in aboveOrEqualC) ):
    print("None")
elif(cp1 != 'A'):
    print(id2)
elif(cp2 != 'A'):
    print(id1)
elif(cal11 not in aboveOrEqualC or cal21 not in aboveOrEqualC):
    print(id2)
elif(cal12 not in aboveOrEqualC or cal22 not in aboveOrEqualC):
    print(id1)
elif(gpax1 > gpax2):
    print(id1)
elif(gpax2 > gpax1):
    print(id2)
elif(cal11 > cal12):
    print(id2)
elif(cal12 > cal11):
    print(id1)
elif(cal21 > cal22):
    print(id2)
elif(cal22 > cal21):
    print(id1)
else:
    print("Both")