from collections import deque
import sys
input = sys.stdin.readline

def BFS(start):
    vis = set()
    queue = deque([(start, 0)])
    C = [1e9]*101
    while queue:
        temp, cnt = queue.popleft()
        if temp not in vis:
            vis.add(temp)
            C[temp] = min(C[temp], cnt)
            for s in graph[temp]:
                if s < 101 and s not in vis:
                    queue.append((s, cnt+1))
    return C

def snakes_and_ladders(graph, a, b):
    for i in range(a-1, a-7, -1):
        if 0 < i < 101:
            idx = graph[i].index(a)
            graph[i][idx] = b
    return graph

n, m = map(int, input().split())
graph = {i:[i+1, i+2, i+3, i+4, i+5, i+6] for i in range(1, 101)}

for _ in range(n+m):
    a, b = map(int, input().split())
    graph = snakes_and_ladders(graph, a, b)

C = BFS(1)
print(C[100])