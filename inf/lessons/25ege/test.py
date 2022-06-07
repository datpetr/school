def f(n):
    num = n
    list_simple = []
    simple = 2
    while num > 1 and simple < int(n ** 0.5) + 1:
        if num % simple == 0:
            list_simple.append(simple)
            num /= simple
        else:
            simple += 1
    return list(map(str, list_simple))


a = []
count = 0
for i in range(4000000, 6000000):
    x = f(i)
    for i in x:
        if i not in '23':
            break
    else:
        if x.count('2') % 2 != 0 and x.count('3') % 2 == 0:
            count += 1
            a.append([i, x])

print(count, a)