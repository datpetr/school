p_start, p_end = 3, 38
q_start, q_end = 21, 57

mx_a = 0

for x in range(1, 100):
    for a in range(1, 100):
        if ((q_start <= x <= q_end) <= (p_start <= x <= p_end)) <= (not(0 <= x <= a)):
            mx_a = a

print(mx_a)
