a,b,c,d = [float(e) for e in input().split()]
maximum = a
minimum = a
if b > maximum:
  maximum = b
if c > maximum:
  maximum = c
if d > maximum:
  maximum = d
if b < minimum:
  minimum = b
if c < minimum:
  minimum = c
if d < minimum:
  minimum = d
s = a+b+c+d-maximum-minimum
avr = s / 2

print(round(avr,2))