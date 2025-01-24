from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
vectors = defaultdict(list)
res = []

for _ in range(n):
    x, y, z = map(int, input().split())
    if x * y == 0:
        if y == 0 and x > 0:
            direction = 0
            m = 0
        elif y == 0 and x < 0:
            direction = 180
            m = 0
        elif x == 0 and y > 0:
            direction = 90
            m = float('inf')
    else:
        m = y / x
        direction = 1
    vectors[(m, direction)].append((x, y, z))

for key, val in vectors.items():
    if key[1] == 0:
        blind = -1
        val.sort(key=lambda x: x[0])
    elif key[1] == 180:
        blind = -1
        val.sort(key=lambda x: -x[0])
    elif key[1] == 90:
        blind = -1
        val.sort(key=lambda x: x[1])
    elif key[1] == 1:
        blind = -1
        val.sort(key=lambda x: (x[0]**2) + (x[1]**2))
    
    for v in val:
        if v[2] <= blind:
            res.append((v[0], v[1]))
        blind = max(v[2], blind)

res.sort(key=lambda x: (x[0], x[1]))
for r in res:
    print(r[0], r[1])