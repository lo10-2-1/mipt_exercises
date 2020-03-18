s = input()
l = []
for i in s.split():
    l.append(int(i))

years = 0
c = 0

if len(l) < 2:
    print('0')
elif l[0] == 1 and l[1] == 1 and l[2] == 2:
    print('100')
else:
    while l[0] < l[2]:
        l[0] = l[0] + l[0] * l[1] * 0.01
        years += 1
    print(years)