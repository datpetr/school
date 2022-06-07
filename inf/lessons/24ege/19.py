f = open('files/k7-97.txt').readline()

mx = 0
count = 0

for i in f:
    if i == 'C':
        count += 1
    else:
        if count > mx:
            mx = count
        count = 0

print(mx)
