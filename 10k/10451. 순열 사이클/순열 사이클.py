from collections import deque

def BFS(start):
    vis = set()
    queue = deque([start])
    while queue:
        temp = queue.popleft()
        if temp not in vis:
            vis.add(temp)
            queue.append(graph[temp])
    return vis

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    graph = {i:A[i-1] for i in range(1, n+1)}
    cnt = 0 ; V = set()
    for k in range(1, n+1):
        if k not in V:
            V.update(BFS(k))
            cnt += 1
    print(cnt)