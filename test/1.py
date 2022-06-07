count = 0

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        for g in range(2):
                            for h in range(2):
                                if (((not (a and b)) or d) and c) and (((not (c and d)) or f) and e) and (((not (e and f)) or h) and g):
                                    count += 1

print(count)


# def p(n, m):
#     count = 0
#     t = 2
#     while n > 0:
#         t *= n % m
#         count += n
#         n //= m
#
#     return count, t
#
#
# print(p(35, 8))