import sys
input = sys.stdin.readline

n = int(input())
C = [[0]*500 for _ in range(500)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            C[i][j] = 1
cnt = 0
for c in C:
    cnt += c.count(1)
print(cnt)