import math, sys
input = sys.stdin.readline

def dist(x1, y1, x2, y2):
    return math.sqrt(((x1-x2)**2) + ((y1-y2)**2))

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
x1, y1 = map(float, input().split())
edge = []
temp = [(x1, y1)]
res = 0
for i in range(1, n):
    x, y = map(float, input().split())
    for j in range(i):
        edge.append((dist(x, y, temp[j][0], temp[j][1]), j, i))
    temp.append((x, y))

edge.sort()
root = [i for i in range(n)] ; rank = [1]*n
for weight, node1, node2 in edge:
    if find(node1) != find(node2):
        res += weight
        union(node1, node2)

print(f"{res:.2f}")