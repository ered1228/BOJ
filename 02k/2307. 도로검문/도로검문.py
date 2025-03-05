import heapq, sys
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(st, tracing):
    distance = [float('inf')]*(n+1)
    distance[st] = 0
    queue = []
    heapq.heappush(queue, (0, st))
    temp = defaultdict(int)
    
    while queue:
        cost, loc = heapq.heappop(queue)
        if cost > distance[loc]:
            continue
        
        for y, z in graph[loc]:
            n_cost = cost + z
            if n_cost < distance[y]:
                distance[y] = n_cost
                heapq.heappush(queue, (n_cost, y))
                temp[y] = loc
    
    if not tracing:
        return distance[n]
    else:
        if distance[n] == float('inf'):
            return float('inf'), []
        else:
            trace = [n]
            bef = temp[n] ; aft = n
            while bef != st:
                trace.append(bef)
                aft = bef
                bef = temp[aft]
            trace.append(st)
            return distance[n], list(reversed(trace))

n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

res = 0
ori, T = dijkstra(1, True)
if ori == float('inf'):
    print(-1)
else:
    for i in range(len(T)-1):
        a, b = T[i], T[i+1]
        w = None
        for idx, (dy, dz) in enumerate(graph[a]):
            if dy == b:
                w = dz
                del graph[a][idx]
                break
        for idx, (dy, dz) in enumerate(graph[b]):
            if dy == a:
                del graph[b][idx]
                break
        res = max(res, dijkstra(1, False))
        graph[a].append((b, w))
        graph[b].append((a, w))
    if res == float('inf'):
        print(-1)
    else:
        print(res-ori)