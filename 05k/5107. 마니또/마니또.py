from collections import deque

def BFS(g):
    vis = set()
    queue = deque([g])
    while queue:
        temp = queue.popleft()
        if temp not in vis:
            vis.add(temp)
            for i in graph[temp]:
                queue.append(i)
    return vis

cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    else:
        graph = dict()
        for _ in range(n):
            a, b = input().split()
            if a not in graph:
                graph[a] = [b]
            else:
                graph[a].append(b)
            if b not in graph:
                graph[b] = [a]
            else:
                graph[b].append(a)
    V = set() ; ring = 0
    for g in graph:
        if g not in V:
            V.update(BFS(g))
            ring += 1
    print(cnt, ring)
    cnt += 1