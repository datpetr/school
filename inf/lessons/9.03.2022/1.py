f = open('files/24_demo.txt', 'r').readline()

mx = 0
count = 1

for j in range(len(f) - 1):
    if f[j] != f[j + 1]:
        count += 1
        if count > mx:
            mx = count
    else:
        count = 1

print(mx)
