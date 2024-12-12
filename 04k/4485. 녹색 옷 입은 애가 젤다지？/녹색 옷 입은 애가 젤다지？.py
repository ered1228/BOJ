import heapq

def dijkstra(M):
    cost = [[float('inf')]*n for _ in range(n)]
    cost[0][0] = M[0][0]
    queue = []
    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]
    heapq.heappush(queue, (cost[0][0], 0, 0))
    while queue:
        tempc, i, j = heapq.heappop(queue)
        if tempc > cost[i][j]:
            continue
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and tempc + M[ni][nj] < cost[ni][nj]:
                cost[ni][nj] = tempc + M[ni][nj]
                heapq.heappush(queue, (cost[ni][nj], ni, nj))
    return cost[n-1][n-1]

i = 0
while True:
    n = int(input())
    if n == 0:
        break
    else:
        i += 1
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))
        res = dijkstra(M)
        print(f"Problem {i}: {res}")