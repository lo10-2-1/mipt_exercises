x=int(input())
if 99<x<1000:
    hund=x//100
    ten=x//10-hund*10
    one=x-hund*100-ten*10
    x=hund+ten+one
    print(x)
else:
    print('Incorrect')