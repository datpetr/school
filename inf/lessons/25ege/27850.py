def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


count = 0

for i in range(245690, 245757):
    count += 1
    if simple(i):
        print(count, i)
