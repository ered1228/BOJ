dp = [1, 1, 2, 4]
for j in range(4, 68):
    dp.append(dp[j-1]+dp[j-2]+dp[j-3]+dp[j-4])

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])