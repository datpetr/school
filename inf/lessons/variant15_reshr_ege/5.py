def algorithm(n1):
    n = bin(n1)[2:]

    st = ''

    print(n)

    for i in n:
        if not(int(i)):
            st += '1'
        else:
            st += '0'

    return n1 - int(st, 2)


for n in range(128, 256):
    if algorithm(n) == 185:
        print(n)
        break
