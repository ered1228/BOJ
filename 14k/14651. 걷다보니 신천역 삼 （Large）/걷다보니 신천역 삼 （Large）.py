n = int(input())
MOD = 10**9 + 9
dp = [0, 0, 2]
if n == 1:
    print(0)
else:
    for i in range(3, n+1):
        dp.append((dp[-1]*3)%MOD)
    print(dp[-1]%MOD)