import sys, math
input = sys.stdin.readline

def polar_angle(p1, p2):
    return math.atan2(p2[1]-p1[1], p2[0]-p1[0])

def distance(p1, p2):
    return (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2

def ccw_sorting(points):
    anchor = min(points, key=lambda p: (p[1], p[0]))
    sorted_points = sorted(points, key=lambda p: (polar_angle(anchor, p), distance(anchor, p)))
    return sorted_points

def CCW(p1, p2, p3):
    v1 = (p2[0] - p1[0], p2[1] - p1[1])
    v2 = (p3[0] - p2[0], p3[1] - p2[1])
    cross_product = v1[0] * v2[1] - v1[1] * v2[0]
    if cross_product > 0:
        return 1
    elif cross_product < 0:
        return -1
    else:
        return 0

def convex_hull(points):
    stack = []
    stack.append(points[0])
    stack.append(points[1])
    for i in range(2, len(points)):
        if CCW(stack[-2], stack[-1], points[i]) == 1:
            stack.append(points[i])
        else:
            while len(stack) >= 2 and CCW(stack[-2], stack[-1], points[i]) != 1:
                stack.pop()
            stack.append(points[i])
    return stack

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
s_points = ccw_sorting(points)
print(len(convex_hull(s_points)))