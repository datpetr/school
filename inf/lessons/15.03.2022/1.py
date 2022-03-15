slovar = {}

slovar['server'] = {
    'host': '192.168.0.1',
    'port': '80'
}

slovar['conf'] = {
    'ssh': {
        'login': 'Ivan',
        'password': 'admin'
    }
}

for i in slovar.values():
    for j in i:
        print(i, ':', i[j])
