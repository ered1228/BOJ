#한 직선 위에 있으면 -1
#result = 2*(가장 먼 점 사이 거리 - 가장 가까운 점 거리)
import math

def distance(x1, y1, x2, y2):
    d = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    return d

A = []
x1, y1, x2, y2, x3, y3 = map(int, input().split())

ux = (x2 - x1)
uy = (y2 - y1)
vx = (x3 - x1)
vy = (y3 - y1)
cross = (ux * vy) - (uy * vx)

if cross == 0:
    print("-1")
else:
    A.append(distance(x1, y1, x2, y2))
    A.append(distance(x1, y1, x3, y3))
    A.append(distance(x2, y2, x3, y3))
    print(2 * (max(A) - min(A)))