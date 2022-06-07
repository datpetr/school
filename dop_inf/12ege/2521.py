s = 'C' * 50 + 'Г' * 50 + 'Н' * 50

while 'ГС' in s or 'НС' in s or 'ГН' in s:
    if 'ГС' in s:
        s = s.replace('ГС', 'СГ', 1)
    if 'НС' in s:
        s = s.replace('НС', 'СН', 1)
    if 'ГН' in s:
        s = s.replace('ГН', 'НГ', 1)

print(s[11], s[91], s[131])
