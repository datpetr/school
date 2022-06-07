f = open('files/24-197.txt', 'r').readline()

count_zxy = count_zyx = mx = ind_zxy = ind_zyx = 0
a_zxy = ['Z', 'X', 'Y']
a_zyx = ['Z', 'Y', 'X']

for i in range(len(f)):
    if a_zyx[ind_zyx % 3] == f[i]:
        count_zxy += 1
        ind_zyx += 1
    else:
        if count_zyx > mx:
            mx = count_zyx
        ind_zyx = 0

    if a_zxy[ind_zxy % 3] == f[i]:
        count_zxy += 1
        ind_zxy += 1
    else:
        if count_zxy > mx:
            mx = count_zxy
        ind_zxy = 0

print(mx)