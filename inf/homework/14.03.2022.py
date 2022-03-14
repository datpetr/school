import collections.abc


def update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


phone_book = {}
data = input('Input name and phone number: ')

while data != '.':
    data = data.replace(',', '').split()
    if len(data) == 1:
        name = ''.join(data)
        if name in phone_book:
            print('{}: {}'.format(name, phone_book[name]))
        else:
            print("NOT FOUND")
    else:
        name, number = data[0], data[1:]
        if name in phone_book:
            data = update(name, number)
        else:
            phone_book[name] = phone_book.get(name, []) + number
    data = input('Input name and phone number: ')

print(phone_book)
