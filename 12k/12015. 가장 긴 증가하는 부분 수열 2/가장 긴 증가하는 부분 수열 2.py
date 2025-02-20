from bisect import bisect_left

n = int(input())
S = [0] + list(map(int, input().split()))
dp = [0]*(n+1)
mv = [0]

for i in range(1, n+1):
    t = S[i]
    idx = bisect_left(mv, t)
    if idx == len(mv):
        mv.append(t)
    else:
        mv[idx] = t
    dp[i] = idx
print(len(mv)-1)