import heapq, sys
input = sys.stdin.readline

def dijkstra(st):
    distance = [float('inf') for _ in range(n+1)]
    distance[st] = 0
    queue = []
    heapq.heappush(queue, (0, st))
    
    while queue:
        dist, point = heapq.heappop(queue)
        if distance[point] < dist:
            continue      
        for v, w in graph[point]:
            if distance[v] > dist + w:
                distance[v] = dist + w
                heapq.heappush(queue, (distance[v], v))
    
    area = []
    for idx, val in enumerate(distance):
        if val <= m and idx != 0:
            area.append(idx)
    return area

n, m, r = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
it = list(map(int, input().split()))
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

res = 0
for i in range(1, n+1):
    temp = 0
    area = dijkstra(i)
    for a in area:
        temp += it[a-1]
    res = max(res, temp)
print(res)