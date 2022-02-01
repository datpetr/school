def f(x):
    return (90878 ** (2 * x)) / (90878 + 90878 ** (2 * x))


res = 0

for k in range(0, 90879):
    res += f(k / 90878)

print(res)
