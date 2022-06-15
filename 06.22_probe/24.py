f = open('files/24_2.txt', 'r').readline()

f = f.replace('BB', '*')
f = f.replace('DD', '*')
f = f.replace('A', ' ')
f = f.replace('B', ' ')
f = f.replace('D', ' ')
print(f.split())
lengths = [len(i) for i in f.split()]

print(max(lengths) + 1)
