def is_divided(x, a):
    return x % a == 0


A = 1

while True:
    for x in range(1, 100000):
        if not((A < 50) and ((not is_divided(x, A)) <= ((is_divided(x, 10)) <= (not is_divided(x, 12))))):
            break
    else:
        print(A)
        break
    A += 1

# max 30