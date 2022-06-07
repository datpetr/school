s = 'А' * 50 + 'Б' * 110 + 'B' * 100

while 'АБ' in s or 'ВА' in s or 'ВБ' in s:
    s = s.replace('ВА', 'АВ', 1)
    s = s.replace('АБ', 'БА', 1)
    s = s.replace('ВБ', 'БВ', 1)

print(s[44], s[113], s[254])
