n = int(input())
t = list(map(int, input().split()))
t.sort(reverse = True)
dp = [i for i in range(1, n+1)]
res = [dp[j]+t[j] for j in range(n)]
print(max(res)+1)