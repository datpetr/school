from math import pi


def circle_s(r):
    print('formula for the area of a circle is S = π * r^2')
    s = pi * (r ** 2)
    return 's = {} = {}π'.format(s, r ** 2)


def circle_p(r):
    print('formula for the perimeter of a circle is P = 2 * π * r')
    p = 2 * pi * r
    return 'p = {} = {}π'.format(p, 2 * r)


r = int(input())

print(circle_s(r))
print(circle_p(r))
