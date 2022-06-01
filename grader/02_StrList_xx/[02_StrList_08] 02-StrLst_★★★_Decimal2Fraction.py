import math
d = input().split(",")
a1 = int(d[0])
a2 = int('0'+d[1])
a3 = int('0'+d[2])
a4 = int( '0'+d[1]+d[2] )

up = a4-a2
down = int('9'*len(d[2]) + '0'*len(d[1]))

up += a1*down

gcd = math.gcd(up,down)
print(str(up//gcd) + " / " + str(down//gcd))