from itertools import combinations

def triarea(p1, p2, p3):
    X = [p1[0], p2[0], p3[0], p1[0]]
    Y = [p1[1], p2[1], p3[1], p1[1]]
    res = 0
    for i in range(1, 4):
        res += X[i-1]*Y[i] - X[i]*Y[i-1]
    return abs(res/2)
    
n = int(input())
points  = []
area = 0
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

for p1, p2, p3 in combinations(points, 3):
    area = max(area, triarea(p1, p2, p3))
print(area)