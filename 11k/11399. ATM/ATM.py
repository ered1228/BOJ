n = int(input())
P = list(map(int, input().split()))
P.sort()
dp = [P[0]]
for i in range(1, n):
    dp.append(dp[i-1] + P[i])
print(sum(dp))