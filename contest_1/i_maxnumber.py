A=[]
x=-1
m=0

while x!=0:
    x=int(input())
    A.append(x)
    m=max(m, x)

print(m)