def is_divided(x, a):
    return x % a == 0


A = 1

while True:
    for x in range(1, 100000):
        if not(is_divided(A, 40) and (is_divided(780, x)) <= ((not is_divided(A, x)) <= (not is_divided(180, x)))):
            break
    else:
        print(A)
    A += 1

# min 120
