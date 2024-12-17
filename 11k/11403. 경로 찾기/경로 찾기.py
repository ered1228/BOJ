import sys
input = sys.stdin.readline

n = int(input())
adj = [] ; dist = [[0]*n for _ in range(n)]
for _ in range(n):
    adj.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
      if adj[i][j] == 1:
          dist[i][j] = 1
      else:
          dist[i][j] = float('inf')

for k in range(n):
    for s in range(n):
        for e in range(n):
            dist[s][e] = min(dist[s][e], dist[s][k] + dist[k][e])

for i in range(n):
    for j in range(n):
        if dist[i][j] == float('inf'):
            dist[i][j] = 0
        else:
            dist[i][j] = 1

for r in dist:
    print(' '.join(map(str, r)))