def sum_list(B:list):
    '''Суммирует элементы полученных на инпуте массивов (оценки студентов)'''
    summ = 0
    if B:
        for i in B:
            summ += i
    return summ

N = int(input())
if N <= 60:
    A = [[] for i in range(N+1)]
inp = ''

while True:
    try:
        inp = input()
        if inp == '#':
            break
        pair = [int(i) for i in inp.split()]
        if 1 <= pair[1] <= 10:
            A[pair[0]].append(pair[1])
        else:
            break
    except (EOFError, IndexError, TypeError):
        raise SystemExit

M = len(A)
for bypass in range(1, M):
    for k in range(0, M - bypass):
        if sum_list(A[k]) < sum_list(A[k+1]):
            A[k], A[k+1] = A[k+1], A[k]

for grade_list in A:
    grade_list.sort(reverse=True)

for row in A:
    for elem in row:
        print(elem, end=' ')
    print(end='')
    