import sys
input = sys.stdin.readline

n = int(input())
vectors = dict()

for _ in range(n):
    x, y = map(int, input().split())
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
        elif x == 0 and y < 0:
            direction = 270
            m = float('inf')
    else:
        m = y / x
        if y > 0:
            direction = 1
        else:
            direction = -1
    if (m, direction) not in vectors:
        vectors[(m, direction)] = 0
    vectors[(m, direction)] += 1

print(sorted(vectors.items(), key=lambda x : (-x[1]))[0][1])