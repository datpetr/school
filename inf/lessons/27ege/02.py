f = open('files')

n = int(f.readline())
d = 6
dmin = [10001] * d
s = 0

for i in range(n):
    a, b = map(int, f.readline().split())
    s += max(a, b)
    difference = abs(a - b)
    dmin[difference % 6] = min(dmin[difference % 6], difference)

if s % 6 == 0:
    print(s)
else:
    print(s, dmin)
