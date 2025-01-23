import sys
input = sys.stdin.readline

n = int(input())
table = []
for _  in range(n):
    a, b = map(int, input().split())
    table.append((a, b))
table.sort(key=lambda x: (x[1], x[0]))

cnt = 1
start, end = table[0][0], table[0][1]
for i in range(1, n):
    if end <= table[i][0]:
        cnt += 1
        start, end = table[i][0], table[i][1]
print(cnt)