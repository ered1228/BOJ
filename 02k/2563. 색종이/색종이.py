P = [[0 for i in range(101)] for j in range(101)]
cnt = 0
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for xi in range(x, x+10):
        for yi in range(y, y+10):
            P[xi][yi] = 1
            
for k in range(101):
    cnt += P[k].count(1)
    
print(cnt)