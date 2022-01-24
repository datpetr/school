def cipher_ceaser(word, shift):
    return list(dict[(shift + dict.index(i)) % 33] for i in word)


dict = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
print(cipher_ceaser(input().upper(), int(input())))
