import sys
import math
input = sys.stdin.readline

x = 10000
N = [True, True] + [False]*(x-1)
for i in range(4, x+1, 2):
    N[i] = True
for j in range(3, int(math.sqrt(x))+1, 2):
    if N[j] == False:
        for k in range(j*j, x+1, j):
            N[k] = True

n = int(input())
for _ in range(n):
    a = int(input())
    for s in range(a//2, 1, -1):
        if not N[s]:
            if not N[a-s]:
                print(s, a-s)
                break