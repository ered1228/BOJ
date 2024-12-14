import heapq
import sys
input = sys.stdin.readline

def dijkstra(a, b):
    millisec = {node : float('inf') for node in graph}
    millisec[a] = 0
    queue = []
    heapq.heappush(queue, (0, a))
    while queue:
        t, w = heapq.heappop(queue)
        if millisec[w] < t:
            continue
        for nt, nw in graph[w]:
            if nt + t < millisec[nw]:
                millisec[nw] = nt + t
                heapq.heappush(queue, (nt + t, nw))
    if millisec[b] != float('inf'):
        return millisec[b]
    else:
        return 'Roger'

n, m = map(int, input().split())
graph = dict()
for _ in range(m):
    s1, s2, t = input().rstrip().split()
    t = int(t)
    if s1 not in graph:
        graph[s1] = []
    if s2 not in graph:
        graph[s2] = []
    graph[s1].append((t, s2))  

q = int(input())
for _ in range(q):
    a, b = input().rstrip().split()
    if a not in graph or b not in graph:
        print("Roger")
    else:
        print(dijkstra(a, b))