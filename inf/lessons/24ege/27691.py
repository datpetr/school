f = open('files/27691.txt', 'r').readline()

count = 0
mx = 0

for i in f:
    if i == 'A':
        count += 1
    else:
        if count > mx:
            mx = count
        count = 0

print(mx)
