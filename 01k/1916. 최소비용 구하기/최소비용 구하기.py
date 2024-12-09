import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
st, des = map(int, input().split())

spend = [float('inf')]*(n+1)
spend[st] = 0
queue = []
heapq.heappush(queue, (0, st))

while queue:
    temp_s, temp_loc = heapq.heappop(queue)
    if temp_s > spend[temp_loc]:
        continue
    for v, w in graph[temp_loc]:
        if temp_s + w < spend[v]:
            spend[v] = temp_s + w
            heapq.heappush(queue, (spend[v], v))

print(spend[des])