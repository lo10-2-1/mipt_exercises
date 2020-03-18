x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

if 0<x1<9 and 0<y1<9 and 0<x2<9 and 0<y2<9:
    if x1==x2:
        print('YES')
    elif y1==y2:
        print('YES')
    elif x1-x2==y1-y2 or x2-x1==y2-y1 or x2-x1==y1-y2 or x1-x2==y2-y1:
        print('YES')
    else:
        print('NO')
else:
    print('Incorrect')