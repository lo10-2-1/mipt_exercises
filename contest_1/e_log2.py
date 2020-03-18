n=int(input())
k=1
begin=2

while n<=10000:
    while begin<=n:
        begin=begin*2
        k+=1
    break

print(k)