n = int(input())
card = []
points = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}

for _ in range(n):
    low = list(map(str, input().split()))
    card.append(low)
if n == 1:
    print(points[card[0][0][0]])
else:
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[n-1][0] = points[card[n-1][0][0]]
    for i in range(n-2, -1, -1):
        dp[i][0] = dp[i+1][0] + points[card[i][0][0]]
    for j in range(1, n):
        dp[n-1][j] = dp[n-1][j-1] + points[card[n-1][j][0]]

    for k in range(n-2, -1, -1):
        for l in range(1, n):
            dp[k][l] = max(dp[k+1][l], dp[k][l-1]) + points[card[k][l][0]]
    print(dp[0][n-1])