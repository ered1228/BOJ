import sys
input = sys.stdin.readline
import heapq

def dijkstra(graph, k):
    distance = [float('inf') for _ in range(n+1)]
    distance[k] = 0
    queue = []
    heapq.heappush(queue, (0, k))
    
    while queue:
        dist, point = heapq.heappop(queue)
        if distance[point] < dist:
            continue
        
        for v, w in graph[point]:
            if distance[v] > dist + w:
                distance[v] = dist + w
                heapq.heappush(queue, (distance[v], v))

    return distance

n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
k = int(input())
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

shortdist = dijkstra(graph, k)

for i in range(1, n+1):
    if shortdist[i] == float('inf'):
        print("INF")
    else:
        print(shortdist[i])