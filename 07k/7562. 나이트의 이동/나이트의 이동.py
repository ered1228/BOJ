from collections import deque
import sys
input = sys.stdin.readline

def BFS(graph, start, target):
    visited = set()
    queue = deque([(start, 0)])
    
    while queue:
        temp, cnt = queue.popleft()
        if temp == target:
            return cnt
        else:
            if temp not in visited:
                visited.add(temp)
                for s in graph[temp]:
                    if s not in visited:
                        queue.append((s, cnt+1))

def next_knight(x, y, I):
    next_cell = []
    candidate_next_cell = [(x+2, y+1), (x+2, y-1), (x+1, y-2), (x+1, y+2), 
                           (x-1, y-2), (x-1, y+2), (x-2, y-1), (x-2, y+1)]
    for c in candidate_next_cell:
        if (0 <= c[0] < I) and (0 <= c[1] < I):
            next_cell.append(c)
    return next_cell

T = int(input())

for _ in range(T):
    I = int(input())
    tx, ty = map(int, input().split())
    gx, gy = map(int, input().split())
    graph = {(i, j):[] for i in range(I) for j in range(I)}
    
    for l in range(I):
        for c in range(I):
            next_cell = next_knight(l, c, I)
            for point in next_cell:
                graph[(l, c)].append(point)
    
    print(BFS(graph, (tx, ty), (gx, gy)))