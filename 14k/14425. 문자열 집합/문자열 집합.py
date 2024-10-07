import sys
input = sys.stdin.readline

n, m = map(int, input().split())
S = []
for _ in range(n):
    a = str(input())
    S.append(a)
cnt = 0
S = set(S)
for i in range(m):
    b = str(input())
    if b in S:
        cnt += 1
print(cnt)