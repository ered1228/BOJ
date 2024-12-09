from collections import deque

F, S, G, U, D = map(int, input().split())
queue = deque([])
vis = set()
queue.append((S, 0))
C = [float('inf')]*(F+1)

while queue:
    temp, cnt = queue.popleft()
    if temp not in vis:
        vis.add(temp)
        C[temp] = min(C[temp], cnt)
        if temp == G:
            break
        for s in [temp+U, temp-D]:
            if 0 < s <= F:
                queue.append((s, cnt+1))

if C[G] == float('inf'):
    print('use the stairs')
else:
    print(C[G])