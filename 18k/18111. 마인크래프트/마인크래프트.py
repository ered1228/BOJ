import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = []
for _ in range(n):
    row = list(map(int, input().split()))
    ground.append(row)
    
time = [0]*257 ; b_list = [b]*257

for h in range(257):
    for x in range(n):
        for z in range(m):
            coordinate = ground[x][z]
            if h < coordinate:
                time[h] += 2*(coordinate-h)
                b_list[h] += coordinate-h
            elif h > coordinate:
                time[h] += h-coordinate
                b_list[h] -= h-coordinate
    if b_list[h] < 0:
        time[h] = float('inf')

res = sorted(enumerate(time), key=lambda x : (x[1], -x[0]))[0]
print(res[1], res[0])