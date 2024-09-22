import math

def is_square(n):
    d = int(math.sqrt(n))
    if d*d == n:
        return True
    else:
        return False

def f(n):
    P = []
    res = 0
    for i in range(1, int(math.sqrt(n)+1)):
        if n % i == 0:
            P.append(i)    
    for p in P:
        if p % 2 == 0 and (n // p) % 2 == 0:
            res += 1
        elif p % 2 == 1 and (n // p) % 2 == 1:
            res += 1
    return res
                
n = int(input())
square = [i*i for i in range(1, 1000001)]
cnt = 0

if n in square:
    print(-1)
else:
    for i in square:
        if i < n and is_square(n-i):
                cnt += 1
    if cnt % 2 == 0:
        cnt //= 2
    else:
        cnt = (cnt // 2) + 1
    cnt += f(n)
    print(cnt)