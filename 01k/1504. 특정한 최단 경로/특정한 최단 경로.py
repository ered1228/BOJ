import heapq, sys
input = sys.stdin.readline

def dijkstra(st, ed):
    dis = [float('inf')]*(n+1)
    dis[st] = 0
    queue = []
    heapq.heappush(queue, (0, st))
    while queue:
        temp_dis, temp_node = heapq.heappop(queue)
        if dis[temp_node] < temp_dis:
            continue
        for next_node, next_dis in graph[temp_node]:
            cost = temp_dis + next_dis
            if cost < dis[next_node]:
                dis[next_node] = cost
                heapq.heappush(queue, (cost, next_node))
    return dis[ed]

n, e = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

res1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
res2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)
if res1 == float('inf') and res2 == float('inf'):
    print(-1)
else:
    print(min(res1, res2))