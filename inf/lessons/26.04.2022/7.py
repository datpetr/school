# ¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 9))
def dell(n, m):
    return n % m == 0


a = 1
while True:
    for x in range(1, 10000):
        if not((not dell(x, a)) <= ((dell(x, 6)) <= (not dell(x, 9)))):
            break
    else:
        print(a)
    a += 1