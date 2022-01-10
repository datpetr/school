def isprime(n):
    x = n
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


start, end = 3532000, 3532160

for i in range(start, end + 1):
    if isprime(i):
        print(i, i - start + 1)
