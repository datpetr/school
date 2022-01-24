n = 13

dp = [0] * (n + 1)
dp[3] = 1

for i in range(5, 10):
    if (i // 2) * 2 == i and i > 3:
        dp[i] = dp[i - 1] + dp[i // 2] + dp[i - 2]
    elif (i // 2) * 2 == i:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]

print(dp)

for i in range(9):
    dp[i] = 0

print(dp)

for i in range(10, n + 1):
    if (i // 2) * 2 == i and i > 3:
        dp[i] = dp[i - 1] + dp[i // 2] + dp[i - 2]
    elif (i // 2) * 2 == i:
        dp[i] = dp[i - 1] + dp[i // 2]
    else:
        dp[i] = dp[i - 1]


print(dp)
