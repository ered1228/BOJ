import heapq, sys
input = sys.stdin.readline

def dijkstra(st):
    queue = []
    distance = [float('inf')]*(n+1)
    distance[st] = 0
    heapq.heappush(queue, (0, st))
    while queue:
        cost, loc = heapq.heappop(queue)
        if cost > distance[loc]:
            continue
        
        for n_loc, n_cost in graph[loc]:
            if n_cost + cost < distance[n_loc]:
                distance[n_loc] = n_cost + cost
                heapq.heappush(queue, (n_cost + cost, n_loc))
    return distance

n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
x, z = map(int, input().split())
l = int(input())
P = list(map(int, input().split()))

res = float('inf')
st = dijkstra(x)
ed = dijkstra(z)
for p in P:
    res = min(res, st[p]+ed[p])
print(res) if res != float('inf') else print(-1)