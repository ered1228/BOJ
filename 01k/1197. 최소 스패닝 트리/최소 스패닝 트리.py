import sys
input = sys.stdin.readline

def union(a, b):
    x = find(a)
    y = find(b)
    if rank[x] < rank[y]:
        root[x] = y
    elif rank[x] > rank[y]:
        root[y] = x
    else:
        root[y] = x
        rank[x] += 1

def find(a):
    if a != root[a]:
        root[a] = find(root[a])
    return root[a]

V, E = map(int, input().split())
edge = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

root = [i for i in range(V+1)]
rank = [0]*(V+1)
res = 0
edge.sort()
for w, n1, n2 in edge:
    if find(n1) != find(n2):
        res += w
        union(n1, n2)

print(res)