for x1 in range(1, 50):
    for x2 in range(1, 50):
        for x3 in range(1, 50):
            s = '0' + '1' * x1 + '2' * x2 + '3' * x3 + '0'
            s2 = s
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('1') == 70 and s.count('2') == 56 and s.count('3') == 23:
                print(len(s2))
                exit(0)
