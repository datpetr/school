f = open('files/1.txt', 'r')

a = []

for i in f:
    a.append(i[:-1])

f.close()

mn = 100000000000
mx_amount_sign = 0
sign = ''
s = ''

for i in a:
    if i.count('G') < mn:
        mn = i.count('G')
        s = i

for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    if s.count(i) >= mx_amount_sign:
        sign = i
        mx_amount_sign = s.count(i)

print(sign, mx_amount_sign)
