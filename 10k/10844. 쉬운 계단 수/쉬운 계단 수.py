n = int(input())
MOD = 10**9
dp1 = [1]
dp9 = [1]
dp = [1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, n+1):
    dp1.append(dp[0])
    dp9.append(dp[-1])
    new_dp = [0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(8):
        if j == 0:
            new_dp[j] = dp1[-2] + dp[1]
        elif j == 7:
            new_dp[j] = dp[6] + dp9[-2]
        else:
            new_dp[j] = dp[j-1] + dp[j+1]
    dp = new_dp

print((sum(dp) + dp9[-1]) % MOD)