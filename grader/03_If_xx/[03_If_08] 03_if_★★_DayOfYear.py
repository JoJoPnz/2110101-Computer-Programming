d = int(input())
m = int(input())
y = int(input())-543

month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
if(y%400==0 or (y%100!=0 and y%4==0)):
  month[2] = 29

x = sum(month[0:m])+d
print(x)