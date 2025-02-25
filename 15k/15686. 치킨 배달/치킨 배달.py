from itertools import combinations
import sys
input = sys.stdin.readline

def ch_dist(city, nch):
    dist = 0
    for hi, hj in house:
        hd = float('inf')
        for ci, cj in nch:
            hd = min(hd, abs(hi-ci) + abs(hj-cj))
        dist += hd
    return dist

n, m = map(int, input().split())
city = [] ; house = [] ; chicken = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            house.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))
    city.append(row)
    
res = float('inf')
new_chicken = combinations(chicken, m)
for nch in new_chicken:
    #for ci, cj in nch:
        #city[ci][cj] = 0
    res = min(res, ch_dist(city, nch))
    #backtracking
    #for ci, cj in nch:
        #city[ci][cj] = 2
print(res)