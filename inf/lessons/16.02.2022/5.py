def f(x, h):
    if 80 > x >= 56 and h == 4:
        return True
    else:
        if x < 56 and h == 4:
            return False
        else:
            if x >= 56:
                return False
    if h % 2 == 1:
        return f(x + 1, h + 1) or f(x * 3, h + 1)
    else:
        return f(x + 1, h + 1) and f(x * 3, h + 1)


for s in range(1, 56):
    if f(s, 1):
        print(s)
