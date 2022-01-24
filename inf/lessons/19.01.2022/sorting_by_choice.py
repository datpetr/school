k = [6, 1, 5, 4, 7]

n = len(k)

for i in range(n - 1):
    smallest_index = i
    for j in range(i + 1, n):
        if k[j] < k[smallest_index]:
            smallest_index = j
    k[i], k[smallest_index] = k[smallest_index], k[i]

print(k)
