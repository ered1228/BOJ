n = int(input())
dp = [0, 2, 4]
j = 3
for i in range(3, n+1):
    dp.append(dp[i-1]+j)
    if i % 3 != 0:
        j += 1
print(dp[n])