n = int(input())
A = list(map(int, input().split()))
score = 0
plus = 1
for i in range(n):
    if A[i] == 1:
        score += plus
        plus += 1
    else:
        plus = 1
print(score)