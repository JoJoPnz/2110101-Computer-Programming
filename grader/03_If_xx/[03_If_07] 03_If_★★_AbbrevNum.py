n = int(input())
if(n<1000):
    print(n)
elif(n<10000):
    print(str(round(n / 1000, 1))+"K")
elif(n<1000000):
    print(str(int(round(n,-3)/1000))+"K")
elif(n<10000000):
    print(str(round(n / 1000000, 1)) + "M")
elif(n<1000000000):
    print(str(int(round(n,-6)/1000000))+"M")
elif(n<10000000000):
    print(str(round(n / 1000000000, 1)) + "B")
else:
    print(str(int(round(n, -9) / 1000000000)) + "B")