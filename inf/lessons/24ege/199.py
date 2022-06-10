f = open('files/24-197.txt', 'r').readline()

a_x_y = []
a_z_y = []
for i in 'XYZ':
    a_x_y.append('X{}X'.format(i))
    a_z_y.append('Y{}Y'.format(i))

for i in a_x_y:
    f = f.replace(i, '*')

for i in a_z_y:
    f = f.replace(i, '*')

for i in 'XYZ':
    f = f.replace(i, ' ')
lengts = [len(_) for _ in f.split()]
print(max(lengts))
