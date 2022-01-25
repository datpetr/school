st = '1' + '0' * 80

while '10' in st or '1' in st:
    if '10' in st:
        st = st.replace('10', '001', 1)
    elif '1' in st:
        st = st.replace('1', '000', 1)

print(st.count('0'))
