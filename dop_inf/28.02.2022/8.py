from itertools import permutations

a = set(list(permutations('РОСАМАХА', 8)))
a_vowelsv = set(list(permutations('ОА', 2)))
a_consonants = set(list(permutations('РСМХ', 2)))

r_amount = 'РОСАМАХА'.count('Р')
s_amount = 'РОСАМАХА'.count('С')
a_amount = 'РОСАМАХА'.count('А')
m_amount = 'РОСАМАХА'.count('М')
h_amount = 'РОСАМАХА'.count('Х')
o_amount = 'РОСАМАХА'.count('О')

count = 0

for i in a:
    if ((i.count('Р') == r_amount) and (i.count('C') == s_amount) and
            (i.count('А') == a_amount) and (i.count('М') == m_amount) and
            (i.count('Х') == h_amount) and (i.count('О') == o_amount)):
        count += 1

print(count)
