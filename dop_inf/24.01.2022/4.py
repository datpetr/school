n = 15

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, 11):
    if (i // 3) * 3 == i and (i > 2):
        dp[i] = dp[i - 1] + dp[i // 3] + dp[i - 2]
    elif (i > 2):
        dp[i] = dp[i - 1] + dp[i - 2]
    else:
        dp[i] = dp[i - 1]

print(dp)

for i in range(10):
    dp[i] = 0

print(dp)

for i in range(11, n + 1):
    if i == 14:
        dp[i] = 0
    elif (i // 3) * 3 == i and (i > 2):
        dp[i] = dp[i - 1] + dp[i // 3] + dp[i - 2]
    elif (i > 2):
        dp[i] = dp[i - 1] + dp[i - 2]
    else:
        dp[i] = dp[i - 1]

print(dp)

# овтет: 252
