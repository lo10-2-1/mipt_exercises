s = input()
l = []
for i in s.split():
    l.append(int(i))

if l[2] < 0:
    print('Incorrect')
elif l[0]**2 + l[1]**2 > l[2]**2:
    print('NO')
else:
    print('YES')