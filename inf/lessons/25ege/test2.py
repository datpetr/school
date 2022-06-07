def f(x, a1, a2):
    return ((8 <= x <= 12) == (4 <= x <= 30)) <= (not (a1 <= x <= a2))


s = []
for a1 in range(-100, 110):
    for a2 in range(-100, 110):
        flag = True
        for x in range(-100, 110):
            if not(f(x, a1, a2)):
                flag = False
                break
        if flag:
            s.append(a2 - a1)

print(max(s) + 1)
