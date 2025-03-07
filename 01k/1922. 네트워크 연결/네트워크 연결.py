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

n = int(input())
m = int(input())
edge = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

root = [i for i in range(n+1)]
res = 0
edge.sort()
for cost, node1, node2 in edge:
    if find(node1) != find(node2):
        union(node1, node2)
        res += cost

print(res)