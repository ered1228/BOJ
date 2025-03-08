import heapq, sys
input = sys.stdin.readline

def dijkstra(st, ed, resnum, y):
    queue = []
    distance = [float('inf')]*(n+1)
    distance[st] = 0
    heapq.heappush(queue, (0, st))
    while queue:
        cost, loc = heapq.heappop(queue)
        if cost > distance[loc]:
            continue
        
        for n_loc, n_cost in graph[loc]:
            if resnum == 2 and n_loc == y:
                continue
            if n_cost + cost < distance[n_loc]:
                distance[n_loc] = n_cost + cost
                heapq.heappush(queue, (n_cost + cost, n_loc))
    return distance[ed]

n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
x, y, z = map(int, input().split())

res1 = dijkstra(x, y, 1, 0) + dijkstra(y, z, 1, 0)
res2 = dijkstra(x, z, 2, y)
if res1 == float('inf'):
    res1 = -1
if res2 == float('inf'):
    res2 = -1
print(res1, res2)