n = int(input())
dp = [0, 1, 1, 1, 2, 3, 4, 6, 9, 13, 19]
for i in range(11, n+1):
    dp.append(dp[i-1] + dp[i-3])
print(dp[n])