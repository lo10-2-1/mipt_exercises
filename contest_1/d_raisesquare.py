x=int(input())
step=1

if 0<x<10001:
    while step**2<=x:
        print(step**2)
        step+=1
else:
    print('Incorrect')