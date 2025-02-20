from bisect import bisect_left

n = int(input())
S = [0] + list(map(int, input().split()))
dp = [0]*(n+1)
mv = [0]
for i in range(1, n+1):
    val = S[i]
    idx = bisect_left(mv, val)
    dp[i] = idx
    if idx == len(mv):
        mv.append(val)
    else:
        mv[idx] = val
print(len(mv)-1)