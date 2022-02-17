def dell(x, A):
    return x % A == 0


A = 1

while True:
    for x in range(1, 10000):
        if not ((not dell(x, A)) <= (dell(x, 6) <= (not dell(x, 4)))):
            break
    else:
        print(A)
    A += 1
