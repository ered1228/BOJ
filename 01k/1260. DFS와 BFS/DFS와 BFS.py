from collections import deque

def DFS(graph, start):
    visit = []
    stack = [start]
    
    while stack:
        temp = stack.pop()
        if temp not in visit:
            visit.append(temp)
            S = list(set(graph[temp]) - set(visit))
            S.sort(reverse=True)
            for s in S:
                stack.append(s)
    return visit

def BFS(graph, start):
    visit = []
    queue = deque([start])
    
    while queue:
        temp = queue.popleft()
        if temp not in visit:
            visit.append(temp)
            S = list(set(graph[temp]) - set(visit))
            S.sort()
            for s in S:
                queue.append(s)
    return visit

n, m, v = map(int, input().split())

graph = {}
for i in range(1, n+1):
    graph[i] = []

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visit1 = DFS(graph, v) ; visit2 = BFS(graph, v)

print(" ".join(map(str, visit1)))
print(" ".join(map(str, visit2)))