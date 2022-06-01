d,m,y = [int(e) for e in input().split()]
y -= 543
n = 31
if m in [4,6,9,11] :
  n = 30
elif m in [2] :
  if y % 400 == 0 or y % 4 == 0 and y % 100 != 0 :
    n = 29
  else :
    n = 28

d = d+15
if d>n :
  d = d-n
  m += 1
if m>12 :
  m = m-12
  y += 1

y += 543

print(str(d)+'/'+str(m)+'/'+str(y))