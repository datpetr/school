f = open('files/k7a-1.txt').readline()

mx = 0
count = 0

for i in f:
    if i in 'ABC':
        count += 1
    else:
        if count > mx:
            mx = count
        count = 0

print(mx)
