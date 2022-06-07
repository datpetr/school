f = open('files/27699.txt').readline()

mx = count = count2 = 0
a = ['L', 'D', 'R']

for i in range(len(f)):
    if f[i] == a[count2 % 3]:
        count += 1
        count2 += 1
    else:
        if count > mx:
            mx = count
        count = 0
print(mx + 1)
