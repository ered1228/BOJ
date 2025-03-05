import heapq, sys
input = sys.stdin.readline

def Army_of_Dumbledore(st, eds):
    result = 0
    distance = [float('inf')]*(n+1)
    distance[st] = 0
    queue = []
    heapq.heappush(queue, (0, st))
    
    while queue:
        cost, loc = heapq.heappop(queue)
        if cost > distance[loc]:
            continue
        
        for y, z in graph[loc]:
            n_cost = cost + z
            if n_cost < distance[y]:
                distance[y] = n_cost
                heapq.heappush(queue, (n_cost, y))
    
    for ed in eds:
        result += distance[ed]
    return result

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = {i:[] for i in range(1, n+1)}
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    k = int(input())
    friends = list(map(int, input().split()))
    
    total_cost = float('inf') ; res = None
    for num in range(1, n+1):
        temp = Army_of_Dumbledore(num, friends)
        if temp < total_cost:
            total_cost = temp
            res = num
    print(res)