n = int(input())
D = list(map(int, input().split()))
cost = list(map(int, input().split()))

mincost = cost[0]
res = mincost*D[0]
for i in range(1, n-1):
    if cost[i] < mincost:
        mincost = cost[i]
        res += D[i]*mincost
    else:
        res += D[i]*mincost
print(res)