def f(x, h):
    if x >= 100 and h == 4:
        return True
    else:
        if x < 100 and h == 4:
            return False
        else:
            if x >= 100:
                return False
    if h % 2 == 1:
        return f(x + 1, h + 1) or f(x * 3, h + 1) or f(x + 3, h + 1)
    else:
        return f(x + 1, h + 1) and f(x * 3, h + 1) and f(x + 3, h + 1)


k = []

for s in range(1, 100):
    if f(s, 1):
        k.append(s)

print(max(k), min(k))

