import heapq
import sys
input = sys.stdin.readline

A = []
n = int(input().strip())
for i in range(n):
    x = int(input().strip())
    if x != 0:
        heapq.heappush(A, (abs(x), x))
    else:
        if A:
            print(heapq.heappop(A)[1])
        else:
            print(0)