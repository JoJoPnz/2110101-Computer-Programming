Eng = ['A','B','C','D','E','F','G','H','I','J']
x = input()
x1 = x[3]+x[10]+x[17]+x[24]+x[31]
x2 = x[7]+x[12]+x[17]+x[22]+x[27]
x3 = int(x1)+int(x2)+10000
x4 = str((x3//10)%1000)
x5 = (int(x4[0])+int(x4[1])+int(x4[2]))%10+1
x6 = Eng[x5-1]
x7 = x4+x6

print(x7)