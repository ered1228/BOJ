from collections import deque

n = int(input())
ancestor = str(input())
family = {ancestor: []}
for _ in range(n-1):
    a, b = input().split(' - ')
    if a not in family:
        family[a] = []
    if b not in family:
        family[b] = []
    family[a].append(b)

queue = deque([(ancestor, 0)])
width = [0]*n
while queue:
    p, rank = queue.popleft()
    width[rank] += 1
    for np in family[p]:
        queue.append((np, rank+1))

print(max(width))