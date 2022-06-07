f = open('files/24-197.txt', 'r').readline()

a_x_y = []
a_z_y = []
for i in 'XYZ':
    a_x_y.append('X{}Y'.format(i))
    a_z_y.append('Z{}Y'.format(i))

for i in a_x_y:
    f = f.replace(i, '*')

for i in a_z_y:
    f = f.replace(i, '*')

for i in 'XYZ':
    f = f.replace(i, ' ')

print(max([len(_) for _ in f.split()]))
