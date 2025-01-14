n, m = map(int, input().split())
K = list(map(int, input().split()))
dp = [0]*(n+1)

for i in range(m):
    j = 1
    while K[i]*j <= n:
        dp[K[i]*j] = 1
        j += 1

res = 0
for k in range(n+1):
    if dp[k] == 1:
        res += k
print(res)