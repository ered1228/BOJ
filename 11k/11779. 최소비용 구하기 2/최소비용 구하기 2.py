import heapq, sys
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(st, ed):
    distance_list = [float('inf')]*(n+1)
    distance_list[st] = 0
    trace = defaultdict(list)
    queue = []
    heapq.heappush(queue, (0, st))
    while queue:
        dist, loc = heapq.heappop(queue)
        if distance_list[loc] < dist:
            continue
        for v, w in graph[loc]:
            if distance_list[v] > dist + w:
                distance_list[v] = dist + w
                trace[v] = trace[loc] + [v]
                heapq.heappush(queue, (distance_list[v], v))
    return distance_list[ed], trace[ed]

n = int(input())
graph = {i:[] for i in range(1, n+1)}
m = int(input())
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
st, ed = map(int, input().split())

cost, trace = dijkstra(st, ed)
print(cost)
print(len(trace)+1)
print(' '.join(map(str, [st]+trace)))