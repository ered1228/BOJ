from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    ground = deque(list(map(int, input().split())))
    num = ground.popleft()
    count = dict()
    for g in ground:
        if g not in count:
            count[g] = 1
        else:
            count[g] += 1
    sol = 0 ; idx = 0 ; conquer = False
    for key, val in count.items():
        if val > sol:
            sol = val
            idx = key
            if sol > num//2:
                conquer = True
                break
    if conquer:
        print(idx)
    else:
        print("SYJKGW")