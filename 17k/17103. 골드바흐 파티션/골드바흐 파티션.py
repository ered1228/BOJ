import sys
import math
input = sys.stdin.readline

A = [False, False] + [True]*999999
for i in range(2, int(math.sqrt(1000000))+1):
    if A[i]:
        for j in range(i*i, 1000001, i):
            A[j] = False
T = {i for i in range(2, 1000001) if A[i]}

t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in T:
        if i <= n//2 and (n-i) in T:
            cnt += 1
    print(cnt)