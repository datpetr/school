nums = 1, 2, 3
a = sorted(nums) == sorted(nums)
revrsed_nums = reversed(nums)
b = sorted(revrsed_nums) == sorted(revrsed_nums)
print(int(a == b) * 1e10)
