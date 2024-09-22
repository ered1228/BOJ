def fac(x):
    value = 1
    if x == 0:
        value = 1
    else :
        for i in range(1, x+1):
            value *= i
    return value    

T = int(input())

for _ in range (1, T+1):
    k, n = map(int, input().split())
    print(fac(n)//(fac(k)*fac(n-k)))  