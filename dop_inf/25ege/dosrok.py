beg = '12345'
mid = '6'
end = '8'
count_div = 0
ans = []

for i in range(100000):
    for j in range(100000):
        numb = int(beg + str(i) + mid + str(j) + end)
        print(numb)
        if numb % 17 == 0:
            ans.append([numb, numb // 17])
            count_div += 1
            if count_div == 6:
                exit(0)

print(ans)
