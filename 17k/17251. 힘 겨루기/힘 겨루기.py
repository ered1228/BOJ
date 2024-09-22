def pf(r, b):
    if r > b:
        print('R')
    elif b > r:
        print('B')
    else:
        print('X')

n = int(input())
A = list(map(int, input().split()))
m = max(A)
M = []
inx = 0

for a in A:
    if a == m:
        M.append(inx)
    inx += 1
    
if len(M) == 1:
    r = n-1-M[-1]
    b = n-1-r
    pf(r, b)
else:
    r = n-1-M[-1]
    draw = M[-1] - M[0]
    b = n-1-r-draw
    pf(r, b)