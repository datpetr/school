def dell(x, A):
    return x % A == 0


A = 1

while True:
    for x in range(1, 10000):
        if not (dell(70, A) and (dell(x, 28) <= ((not(dell(x, A))) <= (not(dell(x, 21)))))):
            break
    else:
        print(A)
    A += 1
