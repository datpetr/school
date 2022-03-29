s = '>' + '1' * 11 + '2' * 12 + '3' * 30
count = 0

while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '222>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)

for i in s[:-1]:
    count += int(i)
print(count)
