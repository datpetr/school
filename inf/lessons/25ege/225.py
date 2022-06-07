def factors(n):
    a = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a += [i, n // i]

    return sorted(set(a))


amount_answers = count_even = 0
k = 1

while amount_answers < 5:
    s = factors(1_850_000_000 + k)
    for i in s:
        if i % 2 == 0:
            count_even += 1

    if count_even % 2 != 0:
        print(k, count_even)
        amount_answers += 1
    k += 1
    count_even = 0
