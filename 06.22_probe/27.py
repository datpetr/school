f = open('files/27A.txt')

n, k = map(int, f.readline().split())
a = list(map(int, f.readlines()))
f.close()
mx, ind = 0, 0
s, count = 0, 0

for i in range(n):
    s += a[i]
    count += 1
    if s <= k:
        mx = max(mx, count)
    else:
        while s > k:
            s -= a[ind]
            count -= 1
            ind += 1
        mx = max(mx, count)

print(mx)
