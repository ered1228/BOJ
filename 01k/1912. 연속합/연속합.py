n = int(input())
arr = list(map(int, input().split()))

if arr[0] >= 0:
    dp = [arr[0]]
    res = arr[0]
else:
    dp = [0]
    res = 0

for i in range(1, n):
    dp.append(dp[i-1] + arr[i])
    if dp[i] < 0:
        dp[i] = 0
    res = max(dp[i], res)

if res != 0:
    print(res)
else:
    print(max(arr))