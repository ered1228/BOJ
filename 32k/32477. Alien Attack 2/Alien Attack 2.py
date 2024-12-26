import sys
input = sys.stdin.readline

from collections import deque

def BFS(st):
    queue = deque([st])
    vis = set()
    while queue:
        x = queue.popleft()
        if x not in vis:
            vis.add(x)
            for y in graph[x]:
                queue.append(y)
    return vis



n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

V = set() ; m = 0
for i in range(1, n+1):
    if i not in V:
        v = BFS(i)
        m = max(m, len(v))
        V.update(v)

print(m)