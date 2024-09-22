import math

def dist(a, b, c, d):
    return math.sqrt((c-a)**2 + (b-d)**2)

# 1-2-3, 1-3-2, 2-1-3, 2-3-1, 3-1-2, 3-2-1
a, b = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
D = []

d = 0
d += dist(a, b, x1, y1) + dist(x1, y1, x2, y2) + dist(x2, y2, x3, y3)
D.append(d)
d = 0
d += dist(a, b, x1, y1) + dist(x1, y1, x3, y3) + dist(x3, y3, x2, y2)
D.append(d)
d = 0
d += dist(a, b, x2, y2) + dist(x2, y2, x1, y1) + dist(x1, y1, x3, y3)
D.append(d)
d = 0
d += dist(a, b, x2, y2) + dist(x2, y2, x3, y3) + dist(x3, y3, x1, y1)
D.append(d)
d = 0
d += dist(a, b, x3, y3) + dist(x3, y3, x1, y1) + dist(x1, y1, x2, y2)
D.append(d)
d = 0
d += dist(a, b, x3, y3) + dist(x3, y3, x2, y2) + dist(x2, y2, x1, y1)
D.append(d)
print(int(min(D)))