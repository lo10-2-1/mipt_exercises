N = int(input())
if N > 10000:
    print('0')
else:
    A = [0]*N

one = 0
oneplus = 0

for i in A:
    A[i] = int(input())
    if A[i] == 1:
        one += 1
        oneplus = max(oneplus, one)
    else:
        one = 0

print(oneplus)