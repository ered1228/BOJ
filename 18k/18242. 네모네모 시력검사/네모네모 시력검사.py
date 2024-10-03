import sys
input = sys.stdin.readline

n, m = map(int, input().split())
box = []
# LEFT, RIGHT, UP, DOWN
for i in range(n):
    P = str(input())
    for j in range(m):
        if P[j] == '#':
            box.append([i, j])
center = ((box[0][0] + box[-1][0])//2, (box[0][1] + box[-1][1])//2)
if [center[0], box[0][1]] not in box:
    print("LEFT")
elif [center[0], box[-1][1]] not in box:
    print("RIGHT")
elif [box[0][0], center[1]] not in box:
    print("UP")
elif [box[-1][0], center[1]] not in box:
    print("DOWN")