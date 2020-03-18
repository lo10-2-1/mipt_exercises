A=[]
x=-1
k=0

while x!=0:
    x=int(input())
    A.append(x)

for i in A:
    if i%2==0:
        k+=1

print(k-1)