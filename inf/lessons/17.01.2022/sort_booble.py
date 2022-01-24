k = list(map(int, input().split()))

count = 0
count_permutations = 0

for _ in k:
    count += 1

for i in range(count - 1):
    for j in range(count - i - 1):
        if k[j] > k[j + 1]:
            count_permutations += 1
            k[j], k[j + 1] = k[j + 1], k[j]

print(k)
print(count_permutations)
