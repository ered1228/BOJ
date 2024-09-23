from bisect import bisect_left, bisect_right

n = int(input())
score = [0]*n

for i in range(n):
    a = int(input())
    score[i] = a

scoreset = list(set(score))
scoreset.sort()
scoreset.remove(scoreset[-1])
scoreset.remove(scoreset[-1])
bronze = max(scoreset)

score.sort()
cnt = bisect_right(score, bronze) - bisect_left(score, bronze)
print(bronze, cnt)