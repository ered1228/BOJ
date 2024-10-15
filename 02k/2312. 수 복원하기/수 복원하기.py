import math
import sys
input = sys.stdin.readline

def pf(n):
    P = []
    Exp = []
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n = n // 2
    if cnt > 0:
        P.append(2)
        Exp.append(cnt)
    for i in range(3, int(math.sqrt(n)+1), 2):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        if cnt > 0:
            P.append(i)
            Exp.append(cnt)
    if n > 2:
        P.append(n)
        Exp.append(1)
    return [P, Exp]

t = int(input())
for _ in range(t):
    n = int(input())
    PF = pf(n)
    for k in range(len(PF[0])):
        print(PF[0][k], PF[1][k])