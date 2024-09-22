def facmod(n, m):
    res = 1
    for i in range(1, n+1):
        res = (res*i) % m
    print(res)

n, m = map(int, input().split())
if m <= n:
    print(0)
else:
    facmod(n, m)