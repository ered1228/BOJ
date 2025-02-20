import sys, heapq
input = sys.stdin.readline

def dijkstra(k):
    distance = [float('inf') for _ in range(n+1)]
    distance[k] = 0
    queue = []
    heapq.heappush(queue, (0, k))   
    while queue:
        dist, point = heapq.heappop(queue)
        if distance[point] < dist:
            continue
        for v in graph[point]:
            if distance[v] > dist + 1:
                distance[v] = dist + 1
                heapq.heappush(queue, (distance[v], v))
    return distance

n, m, k, x = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

distance = dijkstra(x)
minus = True

for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        minus = False
if minus:
    print(-1)