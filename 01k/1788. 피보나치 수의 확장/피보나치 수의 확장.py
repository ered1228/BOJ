n = int(input())
# 절댓값을 1,000,000,000으로 나눈 나머지
plus_fibo = [0, 1, 1, 2]
MOD = 1000000000
if n == 0:
    print(0)
    print(0)
elif n > 0:
    for i in range(4, n+1):
        plus_fibo.append((plus_fibo[i-1]%MOD) + (plus_fibo[i-2]%MOD))
    print(1)
    print(plus_fibo[n]%MOD)
else:
    n *= -1
    for i in range(4, n+1):
        plus_fibo.append((plus_fibo[i-1]%MOD) + (plus_fibo[i-2]%MOD))
    res = ((-1)**(n+1)) * plus_fibo[n]
    if res > 0:
        print(1)
        print(res%MOD)
    else:
        print(-1)
        print(abs(res) % MOD) 