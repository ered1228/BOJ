import heapq, sys
input = sys.stdin.readline

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    dist[start] = 0
    
    while queue:
        dis, now = heapq.heappop(queue)
        if dist[now] < dis:
            continue
        
        for ele in graph[now]:
            if ele[0] <= d  and dis + ele[1] < dist[ele[0]]:
                dist[ele[0]] = dis + ele[1]
                heapq.heappush(queue, (dis + ele[1], ele[0]))
    return dist

n, d = map(int, input().split())
dist = [d]*(d+1)
graph = {i:[(i+1, 1)] for i in range(d+1)}

for _ in range(n):
    u, v, w = map(int, input().split())
    if v <= d:
        graph[u].append((v, w))

res_dist = dijkstra(0)
print(res_dist[d])