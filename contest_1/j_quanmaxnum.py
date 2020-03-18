A=[]
x=-1
k=0

while x!=0:
    x=int(input())
    A.append(x)

maxim=0

for p in A:
    if p>maxim:
        maxim=p

for p in A:
    if p==maxim:
        k+=1

print(k)