f = open('files/k7b-2.txt').readline()

mx = count = count2 = 0
a = ['D', 'B', 'A', 'C']

for i in range(len(f)):
    if f[i] == a[count2 % 4]:
        count += 1
        count2 += 1
    else:
        if count > mx:
            mx = count
        count = count2 = 0
print(mx)
