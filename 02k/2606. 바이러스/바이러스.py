from collections import deque

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
    return len(vis)

n = int(input())
m = int(input())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

res = BFS(graph, 1) - 1
print(res)