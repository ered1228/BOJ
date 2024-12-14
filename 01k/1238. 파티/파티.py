import heapq
import sys
input = sys.stdin.readline

def dijkstra(a):
    distance = [float('inf')]*(n+1)
    distance[a] = 0
    q = []
    heapq.heappush(q, (0, a))
    while q:
        temp_dist, village = heapq.heappop(q)
        if temp_dist > distance[village]:
            continue
        for next_village, next_dist in graph[village]:
            if next_dist + temp_dist < distance[next_village]:
                distance[next_village] = next_dist + temp_dist
                heapq.heappush(q, (next_dist + temp_dist, next_village))
    return distance

n, m, x = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

res = 0
go = [dijkstra(j)[x] for j in range(1, n+1)]
back = dijkstra(x)[1:]
for k in range(n):
    res = max(res, go[k] + back[k])
print(res)