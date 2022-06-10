f = open('files/24.txt', 'r').readline()

f = f.replace('AB', '*')
f = f.replace('CB', '*')
f = f.replace('A', ' ')
f = f.replace('B', ' ')
f = f.replace('C', ' ')


lengts = [len(_) for _ in f.split()]
print(max(lengts))
