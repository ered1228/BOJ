import heapq
import sys
input = sys.stdin.readline

n = int(input())
A = []
for _ in range(n):
    c = int(input())
    if c == 0:
        if len(A) == 0:
            print(0)
        else:
            print(heapq.heappop(A))
    else:
        heapq.heappush(A, c)