import math

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
    return P, Exp

def Euler_phi(P, Exp, n):
    res = 1
    for i in range(len(Exp)):
        res *= (P[i]**Exp[i]) - (P[i]**(Exp[i]-1))
    return res
        
n = int(input())
if n == 1:
    print(1)
else:
    P, Exp = pf(n)
    print(Euler_phi(P, Exp, n))