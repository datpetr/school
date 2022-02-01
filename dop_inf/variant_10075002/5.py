def func(n):

    st_2 = bin(n)[2:]

    for _ in range(3):
        count_0 = st_2.count('0')
        count_1 = st_2.count('1')

        if count_0 == count_1:
            st_2 += st_2[-1]
        elif count_0 >= count_1:
            st_2 += '1'
        else:
            st_2 += '0'

    return int(int(st_2, 2))


flag = True

for i in range(104, 1000):
    if func(i) % 4 == 0:
        print(i)
        break
