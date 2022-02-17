count = 0

for x in range(1, 30):
    for n in range(30):
        if ((2 ** x) + 1) * (2 ** n) < 1000000000:
            count += 1

print(count)
