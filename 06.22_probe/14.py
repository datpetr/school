n = 2197 ** 50 - 169 ** 35 - 26

count = 0

while n:
    if n % 13 == 12:
        count += 1
    n //= 13

print(count)