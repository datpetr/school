f = open('files/24_demo.txt', 'r').readline()

mx = 0
count = 0

for j in range(len(f)):
    if f[j] == 'X':
        count += 1
        if count > mx:
            mx = count
    else:
        count = 0

print(mx)
