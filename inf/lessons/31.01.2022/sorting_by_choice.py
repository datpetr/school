from random import randint


def algorithm_sorting_choice(a_list):
    n = len(a_list)
    for i in range(n - 1):
        elem = a_list[i]
        i_min = i
        for j in range(i + 1, n):
            if a[j] < a[i]:
                elem = a_list[j]
                i_min = j
        if elem != a[i]:
            a_list[i_min], a_list[i] = a_list[i], a_list[i_min]
    return a_list


a = []

for i in range(10000):
    a.append(randint(-100000000000000, 10000000000000000))

print(algorithm_sorting_choice(a))
