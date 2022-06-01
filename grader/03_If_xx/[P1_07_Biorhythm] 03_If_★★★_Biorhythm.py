import math

def day_feb(y,month):
    if(y%400==0 or (y%100!=0 and y%4==0)):
        month[2] = 29
        return
    month[2] = 28
    return

month = [0,31,28,31,30,31,30,31,31,30,31,30,31,0]

bd,bm,by,d,m,y = [int(e) for e in input().split()]
y -= 543
by -= 543

sum2 = (y-by-1)*365

day_feb(by,month)
sum1 = sum(month[bm+1:])+(month[bm]-bd+1)

day_feb(y,month)
sum3 = sum(month[0:m])+(d-1)

t = sum1+sum2+sum3
phy = math.sin(2*math.pi*t/23)
emo = math.sin(2*math.pi*t/28)
intell = math.sin(2*math.pi*t/33)
print(t,"{:.2f}".format(phy),"{:.2f}".format(emo),"{:.2f}".format(intell))