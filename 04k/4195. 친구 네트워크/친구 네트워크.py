import sys
input = sys.stdin.readline

def find(a):
    if a != root[a]:
        root[a] = find(root[a])
    return root[a]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        root[a] = b
        count[b] += count[a]
        count[a] = 0
    else:
        root[b] = a
        count[a] += count[b]
        count[b] = 0

t = int(input())
for _ in range(t):
    F = int(input())
    root = [0] ; count = [1]
    name_dict = {} ; idx = 1
    for _ in range(F):
        p1, p2 = input().split()
        if p1 not in name_dict:
            name_dict[p1] = idx
            root.append(idx)
            count.append(1)
            idx += 1
        if p2 not in name_dict:
            name_dict[p2] = idx
            root.append(idx)
            count.append(1)
            idx += 1
        
        i, j = name_dict[p1], name_dict[p2]
        if find(i) == find(j):
            print(count[find(i)])
        else:
            union(i, j)
            print(count[find(i)])