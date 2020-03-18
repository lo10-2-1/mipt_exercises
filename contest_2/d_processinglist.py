minimum = 1000
maximum = -1000
middle = 0
thirds = 0
allthirds = 0
number = 0
inp = ''

while True:
    inp = input()
    if '#' in inp:
        break
    number_list = inp.split()
    for string in number_list:
        a = int(string)
        number += 1
        maximum = a if a > maximum else maximum
        minimum = a if a < minimum else minimum
        middle += a
        thirds += a

        if number % 3 == 0:
            allthirds = allthirds + thirds % a
            thirds = 0

middle = round(middle / number, 3)

print(middle, maximum, minimum, allthirds)