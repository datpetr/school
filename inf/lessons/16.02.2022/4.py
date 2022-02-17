def f(x, h):
    if 80 > x >= 56 and h == 2:
        return True
    else:
        if x < 56 and h == 2:
            return False

    return f(x + 1, h + 1) or f(x * 3, h + 1)


for s in range(1, 56):
    if f(s, 1):
        print(s)
        break
