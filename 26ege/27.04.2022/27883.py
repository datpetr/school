f = open('files/27883.txt', 'r')

volume, n = list(map(int, f.readline().split()))
count = s = 0

numbers = list(map(int, f.readlines()))
f.close()
numbers.sort()
print(volume, n)
print(numbers)
a = []
for i in numbers:
    s += i
    a.append(i)
    if s <= volume:
        count += 1
    else:
        s -= i
        break

print(volume - s, count, a[-2])
