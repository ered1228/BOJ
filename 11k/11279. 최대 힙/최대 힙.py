import heapq
import sys
input = sys.stdin.readline

A = []
n = int(input())
for _ in range(n):
    c = int(input())
    if c == 0:
        if len(A) == 0:
            print(0)
        else:
            num = heapq.heappop(A)
            print(-num)
    else:
        heapq.heappush(A, -c)