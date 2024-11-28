import sys
import math
input = sys.stdin.readline

def find_sol(N, a):
    for s in range(2, x+1):
        if not N[s]:
            if not N[a-s]:
                return s, a-s

x = 1000000
N = [True, True] + [False]*(x-1)
for i in range(4, x+1, 2):
    N[i] = True
for j in range(3, int(math.sqrt(x))+1, 2):
    if N[j] == False:
        for k in range(j*j, x+1, j):
            N[k] = True

while True:
    a = int(input())
    if a == 0:
        break
    else:
        p, q = find_sol(N, a)
        print("{} = {} + {}".format(a, p, q))