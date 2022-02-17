a = 4 ** 511
b = 2 ** 511
c = 511

st = bin(a + b - c)[2:]

print(st.count('1'))
