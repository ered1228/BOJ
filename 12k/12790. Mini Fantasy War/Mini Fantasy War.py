import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    lena = 0
    shin = 0
    raiden = 0
    anju = 0
    a, b, c, d, e, f, g, h = map(int, input().split())
    if a + e < 1:
        lena = 1
    else:
        lena = a + e
    
    if b + f < 1:
        shin = 1
    else:
        shin = b + f
    
    if c + g < 0:
        raiden = 0
    else:
        raiden = c + g
    
    anju = d + h
    print(lena + (5*shin) + (2*raiden) + (2*anju))