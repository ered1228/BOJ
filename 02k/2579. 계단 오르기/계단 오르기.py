n = int(input())
f = [0] ; dp = [0]

for _ in range(n):
    f.append(int(input()))
    
if n == 1:
    print(f[1])
elif n == 2:
    print(f[1] + f[2])
else:
    dp.append(f[1])
    dp.append(f[1]+f[2])
    for j in range(3, n+1):
        dp.append(max(dp[j-2]+f[j], dp[j-3]+f[j-1]+f[j]))
    print(dp[n])