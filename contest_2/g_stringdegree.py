string = input()
degree = int(input())

def degree_plus(m:str, n:int):
    m *= n
    return m

def degree_minus(m:str, n:int):
    n = -n
    length = len(m) // n
    result = ''
    if len(m) % n == 0:
        for i in range(len(m)-length):
            if m[i] == m[i+length]:
                result = m[0:length]
            else:
                return 'NO SOLUTION'
        return result
    else:
        return 'NO SOLUTION'

if degree < -1:
    print(degree_minus(string, degree))
elif degree > 1:
    print(degree_plus(string, degree))
else:
    print(string)