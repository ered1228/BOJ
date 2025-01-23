from collections import deque
import sys
input = sys.stdin.readline

def BFS(start):
    res = [0]*(n+1)
    vis = set()
    queue = deque([start])
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if i not in vis:
                vis.add(i)
                queue.append(i)
                res[i] = temp
    return res

n = int(input())
graph = {i:[] for i in range(1, n+1)}
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

res = BFS(1)
for r in res[2:]:
    print(r)