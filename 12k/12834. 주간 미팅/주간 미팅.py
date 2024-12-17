import heapq
import sys
input = sys.stdin.readline

def dijkstra(st, end):
    distance = [float('inf')]*(v+1)
    distance[st] = 0
    queue = []
    heapq.heappush(queue, (0, st))
    while queue:
        dist, loc = heapq.heappop(queue)
        if dist > distance[loc]:
            continue
        for nloc, ndist in graph[loc]:
            if ndist + dist < distance[nloc]:
                distance[nloc] = ndist + dist
                heapq.heappush(queue, (ndist + dist, nloc))
    return -1 if distance[end] == float('inf') else distance[end]          

n, v, e = map(int, input().split())
A, B = map(int, input().split())
home = list(map(int, input().split()))
graph = {i:[] for i in range(1, v+1)}
for _ in range(e):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

res1 = [0]*(n+1)
res2 = [0]*(n+1)
for j in range(1, n+1):
    res1[j] += dijkstra(home[j-1], A)
    res2[j] += dijkstra(home[j-1], B)

print(sum(res1) + sum(res2))