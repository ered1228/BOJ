#LIS
from bisect import bisect_left

n = int(input())
sequence = [0] + list(map(int, input().split()))

D = [0]*(n+1)
M = [0]
for i in range(1, n+1):
    temp = sequence[i]
    idx = bisect_left(M, temp)
    if idx == len(M):
        M.append(temp)
        D[i] = idx
    else:
        M[idx] = temp
        D[i] = idx

print(len(M)-1)