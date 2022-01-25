def is_prime(n):
    if n <= 1:
        return False
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            return False
    return True


start, end = 78000000, 85000001

count = 0

for i in range(3, int(end ** (1 / 4)) + 1):
    if is_prime(i):
        n2 = i ** 4
        while n2 <= end:
            if start <= n2 <= end:
                print(n2, i)
            n2 *= 2
