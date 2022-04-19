# print(int('911', 15))

# count = 0
# for x1 in range(9):
#     for x2 in range(9):
#         for x3 in range(9):
#             for x4 in range(9):
#                 if (x4 - x3) % 5 == 0:
#                     count += 1
#
# print(count)
# for n in range(1, 9):
#     for k in 15, 20, 25:
#         if 1 + (n - 1 + k) % 33 == 1:
#             print(n, k)
# def isint(s):
#     try:
#         int(s)
#         return True
#     except ValueError:
#         return False
#
# count = 0
# for y in range(10, 100):
#     if isint((4 + 28 * y) / 102):
#         print((4 + 28 * y) / 102)
#         count += 1
#
# print(count)

# for x in range(1, 1000):
#     for y in range(1, 1000):
#         if x % 11 == 3 and x %  17 == 2 and y % 11 == 5 and y % 13 == 2:
#             print(x, y)
#             exit(0)

# count = 0
# for x in range(1, 1000000):
#     if (13 * (x ** 2)) % 77 == 4:
#         count += 1
#
# print(co
# def inv(x, m):
#     u = (x, 1)
#     v = (m, 0)
#     while v[0] != 0:
#         q = u[0] // v[0]
#         t = (u[0] % v[0], u[1] - q * v[1])
#         u = v
#         v = t
#     if u[0] != 1:
#         return 0
#     return u[1] % m
#
#
# print(inv(23, 77))

def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(i)
            return False
    return True


print(simple(349))
