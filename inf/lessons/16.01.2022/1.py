file = open('files/1.txt', 'r')
text = file.read()
file.close()

d = {}

for i in text:
    d[i] = d.get(i, 0) + 1

for i in sorted(d):
    print(i, ':', d[i])