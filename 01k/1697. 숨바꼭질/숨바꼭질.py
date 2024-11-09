from collections import deque

def BFS(start, target):
    vis = set()
    queue = deque([(start, 0)])
    
    while queue:
        temp, cnt = queue.popleft()
        if temp == k:
            break
        if temp not in vis:
            vis.add(temp)
            for s in [temp+1, temp-1, temp*2]:
                if s not in vis and s < 100001:
                    queue.append((s, cnt+1))
    return cnt
                    
n, k = map(int, input().split())
if n >= k:
    print(n-k)
else:
    print(BFS(n, k))