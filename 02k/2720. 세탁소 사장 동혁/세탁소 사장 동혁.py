def sol(money):
    Q = money // 25
    money -= Q*25
    D = money // 10
    money -= D*10
    N = money // 5
    money -= N*5
    P = money
    return int(Q), int(D), int(N), int(P)
    
n = int(input())

for _ in range(n):
    money = int(input())
    Q, D, N, P = sol(money)
    print(Q, D, N, P)