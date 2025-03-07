import sys
input = sys.stdin.readline

def union(a, b):
    x = find(a)
    y = find(b)
    if root[x] < root[y]:
        root[x] = y
    elif root[y] < root[x]:
        root[y] = x

def find(a):
    if a != root[a]:
        root[a] = find(root[a])
    return root[a]

n, m = map(int, input().split())
edge = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

root = [i for i in range(n+1)]
edge.sort()
res = 0
way = 0
for cost, node1, node2 in edge:
    if find(node1) != find(node2):
        union(node1, node2)
        way = max(way, cost)
        res += cost

print(res-way)