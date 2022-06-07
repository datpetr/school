import math


filtred = [i + 1 for i in range((-7) ** 4, 7 ** 4, 7 ** 2)]
print(math.ceil(sum(filtred)*1e7/math.factorial(7)) + 1)