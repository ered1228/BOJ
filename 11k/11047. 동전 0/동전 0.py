n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

answer = 0
for c in coins:
    if k >= c:
        answer += k // c
        k = k % c
        if k == 0:
       		break
print(answer)