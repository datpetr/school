def f(n):
    num = n
    list_simple = []
    while num % 2 == 0 or num % 3 == 0:
        if num % 2 == 0:
            list_simple.append(2)
            num //= 2
        if num % 3 == 0:
            list_simple.append(3)
            num //= 3

    if num == 1:
        return list(map(str, list_simple))
    else:
        return []


a = []
count = 0

for i in range(4000000, 6000000 + 1):
    x = f(i)
    if (len(x) != 0 and
            x.count('2') % 2 != 0
            and x.count('3') % 2 == 0
            and x.count('2') != 0
            and x.count('3') != 0):
        a.append([i, x])
        count += 1

print(a)
print(count)
