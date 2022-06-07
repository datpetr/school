beg, end = map(int, input().split())
n_divisors = int(input())

for x in range(beg, end + 1):
    count = 0
    d = (0, 0)
    for i in range(2, int(beg ** 0.5) + 1):
        if x % i == 0:
            d = i, x // i
            if x // i - i != 0:
                count += 2
            else:
                count += 1
        if count > n_divisors:
            break

    if count == n_divisors:
        print(*d)
