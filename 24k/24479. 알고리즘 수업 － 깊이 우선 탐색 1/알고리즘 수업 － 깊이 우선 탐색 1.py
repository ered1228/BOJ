import sys
input = sys.stdin.readline

def DFS(graph, start):
    visited = set()
    order = []
    stack = [start]
    while stack:
        temp = stack.pop()
        if temp not in visited:
            visited.add(temp)
            order.append(temp)
            S = set(graph[temp]) - visited
            for s in S:
                stack.append(s)
    return order

N, M, R = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}
res = [0]*N
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort(reverse=True)

V = DFS(graph, R)
for inx, v in enumerate(V, start=1):
    res[v-1] = inx

for r in res:
    print(r)