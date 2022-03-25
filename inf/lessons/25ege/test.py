def simple(x):
    if x <= 1:
        return False
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True


start, end = 210235, 210300

for n in range(int(start ** (1 / 5)), int(end ** (1 / 5)) + 2):
    x = n ** 4
    if start <= x <= end and simple(n):
        print(n, n ** 2, n ** 3, n ** 4)
