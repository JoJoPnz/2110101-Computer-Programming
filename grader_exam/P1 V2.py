# while len(newword) != 0
# 1)if len(newword) == 1:
#     if len(s) != 0: --> s+= newword
#     else: --> s = newword
#      out.append(s)
#      break      
# 2) เช็ค alphaอยู่ใน dicไหม
#  - ถ้าไม่อยู่เพิ่ม alphaใน s --> เปลี่่ยน newword
#  - ถ้าอยู่ก็เอา sที่เก็บได้ไปappendใน out --> s='' --> เช็คในdic -->
# appendในout -->เปลี่่ยน newword --> break
# ------------------------------------------------------
word = input().lower()
temp = []
n = int(input())
for i in range(n):
    x = input()
    temp.append([len(x),x])
dic = []
for i in sorted(temp)[::-1]:
    dic.append(i[1])

newword = word
s = ''
out = []
while len(newword) != 0:
    if len(newword) == 1:
        if len(s) != 0:
            s += newword
        else:
            s = newword
        out.append(s)
        break
    
    found = False
    for e in dic:
        if newword.find(e) == 0:
            if len(s) != 0:
                out.append(s)
                s = ''
            out.append(e)
            newword = newword[len(e):]
            found = True
            break
    if not found:
        s += newword[0]
        newword = newword[1:]
print(' '.join(out))
            