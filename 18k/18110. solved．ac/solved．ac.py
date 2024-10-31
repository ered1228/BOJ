from collections import deque
import sys
input = sys.stdin.readline

def roundup(x):
    if abs(int(x) - x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

n = int(input())
if n == 0:
    print(0)
else:
    levels = []
    for _ in range(n):
        l = int(input())
        levels.append(l)
    cut = roundup(float(len(levels)) * (0.15))
    levels.sort() ; levels = deque(levels)
    for i in range(cut):
        levels.pop()
        levels.popleft()
    res = sum(levels) / len(levels)
    print(roundup(res))