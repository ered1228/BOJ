from itertools import permutations
import sys
import math
input = sys.stdin.readline

n = list(map(int, input().split()))
A = list(permutations(n, 8))
c = 0

for a in A:
    x = [0]*10
    y = [0]*10
    x[0], y[0] = a[0], 0
    x[1], y[1] = a[1]/math.sqrt(2), a[1]/math.sqrt(2)
    x[2], y[2] = 0, a[2]
    x[3], y[3] = -a[3]/math.sqrt(2), a[3]/math.sqrt(2)
    x[4], y[4] = -a[4], 0
    x[5], y[5] = -a[5]/math.sqrt(2), -a[5]/math.sqrt(2)
    x[6], y[6] = 0, -a[6]
    x[7], y[7] = a[7]/math.sqrt(2), -a[7]/math.sqrt(2)
    x[8], y[8] = a[0], 0
    x[9], y[9] = a[1]/math.sqrt(2), a[1]/math.sqrt(2)
    
    result = True
    for i in range(8):
        x1, y1 = x[i], y[i]
        x2, y2 = x[i+1], y[i+1]
        x3, y3 = x[i+2], y[i+2]
        cross = ((x2 - x1)*(y3 - y2)) - ((y2 - y1)*(x3 - x2))
        if cross < 0:
            result = False
    if result:
        c += 1
print(c)