u = input()
u = u[1:-1]
u1,u2,u3 = [float(e) for e in u.split(", ")]
u = [u1,u2,u3]

v = input()
v = v[1:-1]
v1,v2,v3 = [float(e) for e in v.split(", ")]
v = [v1,v2,v3]

x1 = u1+v1
x2 = u2+v2
x3 = u3+v3
x = [x1,x2,x3]

print(str(u) + ' + ' + str(v) + ' = ' + str(x))