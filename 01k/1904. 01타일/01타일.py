n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for j in range(3, n+1):
    dp[j] = (dp[j-1]+ dp[j-2])%15746

print(dp[n])