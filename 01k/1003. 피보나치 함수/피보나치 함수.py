import sys
input = sys.stdin.readline

dp = [[1, 0], [0, 1]]
for j in range(2, 41):
    dp.append([dp[j-1][0]+dp[j-2][0], dp[j-1][1]+dp[j-2][1]])

T = int(input())
for _ in range(T):
    n = int(input())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        print(dp[n][0], dp[n][1])