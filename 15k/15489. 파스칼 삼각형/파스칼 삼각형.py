import math

n, m, w = map(int, input().split())
res = 0
for i in range(w):
    for j in range(m-1, m-1+i+1):
        res += math.comb(n-1, j)
    n += 1
print(res)