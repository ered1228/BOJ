import math

def dis(x1, y1, x2, y2):
    d = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    return d

W, H, x1, y1, P = map(int, input().split())
x2 = x1 + W
y2 = y1 + H
r = H/2
cnt = 0

for i in range(P):
    px, py = map(int, input().split())
    if y1 <= py and py <= y2:
        if x1 <= px and px <= x2:
            cnt += 1
        elif x2 < px and px <= (x2 + r):
            di = dis(x2, y1+r, px, py)
            if di <= r:
                cnt += 1
        elif (x1 - r) <= px and px <= x1:
            di = dis(x1, y1+r, px, py)
            if di <= r:
                cnt += 1
print(cnt)