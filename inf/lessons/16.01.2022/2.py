f = open('files/24.txt').read().splitlines()

mn = 100000000
s = ''
d = {}

for i in f:
    if i.count('G') < mn:
        mn = i.count('G')
        s = i

for i in s:
    d[i] = d.get(i, 0) + 1

for i in sorted(d, key=lambda x: d[x]):
    print(i, d[i])
