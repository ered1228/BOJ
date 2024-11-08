from collections import deque
import sys
input = sys.stdin.readline

def BFS(graph, start):
    vis = set()
    queue = deque([start])
    while queue:
        temp = queue.popleft()
        if temp not in vis:
            vis.add(temp)
            for s in graph[temp]:
                if s not in vis:
                    queue.append(s)
    return vis

n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

V = set() ; res = 0
for j in range(1, n+1):
    if j not in V:
        v = BFS(graph, j)
        res += 1
        V.update(v)

print(res)