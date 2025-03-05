from itertools import permutations
import sys
input = sys.stdin.readline

def collision(robot, S):
    line = [(robot[0][0], robot[0][1], S[0][0], S[0][1])]
    for i in range(1, n):
        next_line = (robot[i][0], robot[i][1], S[i][0], S[i][1])
        for l in line:
            if is_cross(l, next_line):
                return True
        line.append(next_line)
    return False

def is_cross(l1, l2):
    x1, y1, x2, y2 = l1[0], l1[1], l1[2], l1[3]
    x3, y3, x4, y4 = l2[0], l2[1], l2[2], l2[3]
    cross1 = ((x2 - x1)*(y4 - y1)) - ((y2 - y1)*(x4 - x1))
    cross2 = ((x2 - x1)*(y3 - y1)) - ((y2 - y1)*(x3 - x1))
    cross3 = ((x4 - x3)*(y2 - y3)) - ((y4 - y3)*(x2 - x3))
    cross4 = ((x4 - x3)*(y1 - y3)) - ((y4 - y3)*(x1 - x3))

    if cross1*cross2 < 0 and cross3*cross4 < 0:
        return True
    elif cross1*cross2 == 0 and cross3*cross4 < 0:
        return True
    elif cross1*cross2 < 0 and cross3*cross4 == 0:
        return True
    elif cross1*cross2 == 0 and cross3*cross4 == 0:
        if max(x1, x2) >= min(x3, x4) and max(x3, x4) >= min(x1, x2) and max(y1, y2) >= min(y3, y4) and max(y3, y4) >= min(y1, y2):
            return True
        else:
            return False
    else:
        return False

n = int(input())
robot = [] ; shelter = [] ; sh_num = dict()
for _ in range(n):
    x, y = map(int, input().split())
    robot.append((x, y))
for i in range(n):
    x, y = map(int, input().split())
    shelter.append((x, y))
    sh_num[(x, y)] = i+1

if n == 1:
    print(1)
else:
    sol = None
    P = permutations(shelter, n)
    for S in P:
        if not collision(robot, S):
            sol = S
            for s in sol:
                print(sh_num[s])
            exit()