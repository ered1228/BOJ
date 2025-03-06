import sys
input = sys.stdin.readline

def find(a):
    if root[a] != a:
        root[a] = find(root[a])
    return root[a]

def union(a, b):
    x, y = find(a), find(b)
    if rank[x] < rank[y]:
        root[x] = y
    elif rank[x] > rank[y]:
        root[y] = x
    else:
        root[x] = y
        rank[y] += 1

n = int(input())
edge = []
res = 0
flow_cost = [[0]*n]*n
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(i, n):
        flow_cost[i][j] = row[j]
        flow_cost[j][i] = row[j]
        edge.append((flow_cost[i][j], i, j))

edge.sort()
root = [i for i in range(n)] ; rank = [1]*n
for weight, planet1, planet2 in edge:
    if find(planet1) != find(planet2):
        res += weight
        union(planet1, planet2)

print(res)