from itertools import combinations
import sys
input = sys.stdin.readline

def is_cross(l1, l2):
    x1, y1, x2, y2 = l1[0], l1[1], l1[2], l1[3]
    x3, y3, x4, y4 = l2[0], l2[1], l2[2], l2[3]
    cross1 = ((x2 - x1)*(y4 - y1)) - ((y2 - y1)*(x4 - x1))
    cross2 = ((x2 - x1)*(y3 - y1)) - ((y2 - y1)*(x3 - x1))
    cross3 = ((x4 - x3)*(y2 - y3)) - ((y4 - y3)*(x2 - x3))
    cross4 = ((x4 - x3)*(y1 - y3)) - ((y4 - y3)*(x1 - x3))
    
    if cross1*cross2 < 0 and cross3*cross4 < 0:
        return True
    elif cross1*cross2 == 0 and cross3*cross4 < 0:
        return True
    elif cross1*cross2 < 0 and cross3*cross4 == 0:
        return True
    elif cross1*cross2 == 0 and cross3*cross4 == 0:
        if max(x1, x2) >= min(x3, x4) and max(x3, x4) >= min(x1, x2) and max(y1, y2) >= min(y3, y4) and max(y3, y4) >= min(y1, y2):
            return True
        else:
            return False
    else:
        return False

def union(a, b):
    x = find(a)
    y = find(b)
    if rank[x] < rank[y]:
        root[x] = y
        nodecount[y] += nodecount[x]
        nodecount[x] = 0
    elif rank[x] > rank[y]:
        root[y] = x
        nodecount[x] += nodecount[y]
        nodecount[y] = 0
    else:
        root[y] = x
        rank[x] += 1
        nodecount[x] += nodecount[y]
        nodecount[y] = 0

def find(a):
    if a != root[a]:
        root[a] = find(root[a])
    return root[a]

n = int(input())
line = []
root = [i for i in range(n)] ; rank = [0]*n ; nodecount = [1]*n
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    line.append((x1, y1, x2, y2))

line_pair = combinations([i for i in range(n)], 2)
for i, j in line_pair:
    l1, l2 = line[i], line[j]
    if is_cross(l1, l2) and find(i) != find(j):
        union(i, j) #line i and j are in the same group

group = 0
for nc in nodecount:
    if nc > 0:
        group += 1
print(group)
print(max(nodecount))