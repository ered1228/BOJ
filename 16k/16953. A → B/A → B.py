from collections import deque

def BFS(a, b):
    if a > b:
        return -1
    elif a == b:
        return 1
    else:
        vis = set()
        queue = deque([(a, 1)])
        while queue:
            cur, cnt = queue.popleft()
            if cur == b:
                return cnt
            if cur not in vis:
                vis.add(cur)
                C = [cur*2, (10*cur)+1]
                for c in C:
                    if c <= b and c not in vis:
                        queue.append((c, cnt+1))
        return -1

a, b = map(int, input().split())
print(BFS(a, b))