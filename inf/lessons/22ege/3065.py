mx = 0
for i in range(1, 100000000000000):
    x = i
    a = 2
    b = 3

    while x > 0:
        d = x % 4
        a *= d
        if d < 3:
            b += d
        x //= 4
    
    if a == 23 and b == 16:
        mx = i
        print(i)

print(mx)
