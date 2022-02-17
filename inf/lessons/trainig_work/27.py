a = []

with open('27_A.txt') as f:
    n = int(f.readline())
    for _ in range(n):
        a.append(int(f.readline()))

tail = [1] + [0] * 998
sum_ = 0
count = 0

for x in range(n):
    sum_ += a[n]
    remainder = sum_ % 999

    count += tail[remainder]
    tail[remainder] += 1

print(count)
