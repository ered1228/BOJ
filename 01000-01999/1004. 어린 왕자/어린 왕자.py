import math

t = int(input())
for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for j in range(n):
        cx, cy, r = map(int, input().split())
        d1 = math.sqrt(((x1 - cx)**2) + ((y1 - cy)**2))
        d2 = math.sqrt(((x2 - cx)**2) + ((y2 - cy)**2))
        if d1 > r and d2 < r:
            cnt += 1
        elif d1 < r and d2 > r:
            cnt += 1
    print(cnt)