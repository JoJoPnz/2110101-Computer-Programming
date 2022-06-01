import math
w = float(input())
h = float(input())

x = (math.sqrt(w*h))/60
y = 0.024265*w**0.5378*h**0.3964
z = 0.0333*w**(0.6157-0.0188*math.log(w,10))*h**0.3

print(x)
print(y)
print(z)