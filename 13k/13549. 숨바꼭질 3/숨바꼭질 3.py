import heapq

n, k = map(int, input().split())
dis = [float('inf')]*(100001)
dis[n] = 0
queue = []
heapq.heappush(queue, (0, n))
while queue:
    temp_dis, temp_node = heapq.heappop(queue)
    if dis[temp_node] < temp_dis:
        continue
    for next_node, next_dis in [(2*temp_node, 0), (temp_node-1, 1), (temp_node+1, 1)]:
        if 0 <= next_node <= 100000:
            cost = temp_dis + next_dis
            if cost < dis[next_node]:
                dis[next_node] = cost
                heapq.heappush(queue, (cost, next_node))
print(dis[k])