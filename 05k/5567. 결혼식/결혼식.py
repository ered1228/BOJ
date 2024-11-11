import sys
from collections import deque
input = sys.stdin.readline

def BFS(start):
    vis = set()
    queue = deque([(start, 0)])
    while queue:
        temp, cnt = queue.popleft()
        if temp not in vis and cnt < 3:
            vis.add(temp)
            for s in graph[temp]:
                if s not in vis:
                    queue.append((s, cnt+1))
    return list(vis)

n = int(input())
m = int(input())
graph = {key:[] for key in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ISD = BFS(1)
print(len(ISD)-1)