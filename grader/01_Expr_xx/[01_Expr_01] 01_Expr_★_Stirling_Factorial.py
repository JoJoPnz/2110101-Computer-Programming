import math
n = int(input())
lower = (2*math.pi)**0.5*n**(n+0.5)*math.e**(-n+1/(12*n+1))
upper = (2*math.pi)**0.5*n**(n+0.5)*math.e**(-n+1/(12*n))
print(lower)
print(upper)