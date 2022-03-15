phone_book = {}
data = input('Input name and phone number: ')

while data != '.':
    data = data.replace(',', '').split()
    if len(data) == 1:
        name = ''.join(data)
        if name in phone_book:
            print('{}, {}'.format(name, phone_book[name]))
        else:
            print("NOT FOUND")
    else:
        name, number = data[0].capitalize(), data[1:]
        phone_book[name] = phone_book.get(name, []) + number
    data = input('Input name and phone number: ')

for elem in phone_book:
    print('{}: {}'.format(elem, phone_book[elem]))
