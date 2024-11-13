from collections import deque

def BFS(start):
    queue = deque([(start, 0)])
    vis = set()
    dist = []
    while queue:
        temp, cnt = queue.popleft()
        if temp not in vis:
            vis.add(temp)
            dist.append(cnt) 
            for s in virgo[temp]:
                if s not in vis:
                    queue.append((s, cnt+1))
    return max(dist)
    
virgo = {i:[] for i in range(1, 13)}
for _ in range(12):
    a, b = map(int, input().split())
    virgo[a].append(b)
    virgo[b].append(a)

spica = []
for star in virgo:
    if len(virgo[star]) == 3:
        for t in virgo[star]:
            if len(virgo[t]) == 1:
                spica.append(star)

find = [BFS(s) for s in spica]
if find[0] == 4:
    print(spica[1])
else:
    print(spica[0])