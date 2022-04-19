def f(x, y, h):
    if x + y >= 77 and h == 2:
        return True
    else:
        if x + y < 77 and h == 2:
            return False
    return f(x + 1, y, h + 1) or f(x * 2, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1)


for s in range(1, 70):
    if f(7, s, 1):
        print(s)
        break

