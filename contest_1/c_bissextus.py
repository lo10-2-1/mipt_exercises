n=int(input())

if 0 < n < 100000:
    if n%400==0:
        print('YES')
    elif n%100==0:
        print('NO')
    elif n%4==0:
        print('YES')
    else:
        print('NO')
else:
    print('Incorrect')