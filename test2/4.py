with open('4.txt', 'w+', encoding='utf-8') as f:
    f.write(''.join(str(int((sum([q for q in range(3 ** 2, 3 ** 4, 3 ** 3)])) ** (1/2)))))