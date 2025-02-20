n, m = map(int, input().split())
d = n+m-2
candy = []
for _ in range(n):
    candy.append(list(map(int, input().split())))
dp = [[0]*m for _ in range(n)]
dp[0][0] = candy[0][0]

for k in range(1, d+1):
    for i in range(0, k+1):
        j = k-i
        temp = []
        if not (0 <= i < n and 0 <= j < m):
            continue
        if 0 <= i-1 < n and 0 <= j < m:
            temp.append(dp[i-1][j])
        if 0 <= i < n and 0 <= j-1 < m:
            temp.append(dp[i][j-1])
        dp[i][j] = max(temp) + candy[i][j]

print(dp[n-1][m-1])