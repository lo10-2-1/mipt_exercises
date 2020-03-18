def split_chocolate(A:list):
    '''Splits chocolate bar into pieces with 2 segments.
    In input - two-dimensional list (chocolate bar) with coordinates i; j. i always == 3
    In output - amount of ways of splitting chocolate bar.
    Function is reccurent. We end it when all elements (or all except 1) of a list == 0'''
    am = 0
    if :
        return am
    else:
        if A[i][j] == A[i+1][j] or A[i][j] - 
        am += 1
        A = split_chocolate(A)

N = int(input())
Choc = [[1]*3 for i in range(N)]
amount = split_chocolate(Choc)

print(amount)