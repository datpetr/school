def is_divided(x, a):
    return x % a == 0


A = 1

while True:
    for x in range(1, 100000):
        if not((not is_divided(x, A)) <= (is_divided(x, 6) <= (not is_divided(x, 4)))):
            break
    else:
        print(A)
    A += 1

# max a
