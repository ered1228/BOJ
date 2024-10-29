def APT(k, n):
    if k == 0:
        return n
    else:
        dp = [i for i in range(1, n+1)]
        for _ in range(k):
            new_dp = []
            for j in range(n):
                new_dp.append(sum(dp[:j+1]))
            dp = new_dp
        return dp[n-1]

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(APT(k, n))