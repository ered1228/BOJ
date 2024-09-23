import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
S = [0]*76
for _ in range(n):
    a = int(input())
    S[a] += 1

b = 0
c = 0
cnt = 0
for i in range(75, -1, -1):
    if S[i] > 0:
        c += 1
    if c == 3:
        b = i
        cnt = S[i]
        break
print(b, cnt)