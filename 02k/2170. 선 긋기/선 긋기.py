import sys
input = sys.stdin.readline

n = int(input())
cor = []
for _ in range(n):
    x, y = map(int, input().split())
    cor.append((x, y))

cor.sort(key = lambda x : x[0])
st, end = cor[0][0], cor[0][1]
length = 0
for i in range(1, n):
    if st <= cor[i][0] <= end:
        end = max(end, cor[i][1])
    else:
        length += end - st
        st = cor[i][0]
        end = cor[i][1]

length += end - st
print(length)