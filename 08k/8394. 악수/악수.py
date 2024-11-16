dp = [0, 1, 2]
n = int(input())

for j in range(3, n+1):
    dp.append((dp[j-1]+dp[j-2])%10)

print(dp[n])