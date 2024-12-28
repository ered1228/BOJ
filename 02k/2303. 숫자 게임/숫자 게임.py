from itertools import combinations as comb

def game(A):
    temp = comb(A, 3)
    res = 0
    for num in temp:
        res = max(int(str(sum(num))[-1]), res)
    return res

n = int(input())
score = [0]*(n+1)
for i in range(1, n+1):
    A = list(map(int, input().split()))
    score[i] = (game(A), i)

score = sorted(score[1:], key=lambda x: (-x[0], -x[1]))
print(score[0][1])