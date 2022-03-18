f = open('files/k7b-1.txt').readline()

mx = 0
count = 1
count2 = 0
a = ['E', 'A', 'B']

for i in range(len(f)):
    if f[i] == a[count2 % 3]:
        count += 1
        count2 += 1
    else:
        if count > mx:
            mx = count
        count = 1
print(mx)
