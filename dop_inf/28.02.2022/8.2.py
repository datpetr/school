from itertools import permutations

a = set(list(permutations('РОСАМАХА', 8)))
a2 = set(list(permutations('ОА', 2)))
a3 = set(list(permutations('РСМХ', 2)))

a_vowelsv = []
a_consonants = []

for i in a2:
    a_vowelsv.append(i[0] + i[1])

for i in a3:
    a_consonants.append(i[0] + i[1])

count = 0
words = []

for i in a:
    flag = True
    for j in range(len(i) - 1):
        if ((i[j] + i[j + 1]) in a_vowelsv) or ((i[j] + i[j + 1]) in a_consonants):
            flag = False
            break
    if flag:
        count += 1

print(count)
