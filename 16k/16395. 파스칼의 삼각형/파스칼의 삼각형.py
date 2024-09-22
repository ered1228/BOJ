import math
n, k = map(int, input().split())
if n == 1 and k == 1:
    print(1)
else:
    s = math.comb(n-1, k-1)
    print(s)