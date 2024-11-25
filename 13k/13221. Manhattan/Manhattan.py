x, y = map(int, input().split())
k = int(input())
d = float('inf') ; res = (0, 0)
for _ in range(k):
    a, b = map(int, input().split())
    m = abs(x-a) + abs(y-b)
    if m <= d:
        res = (a, b)
        d = m
print(res[0], res[1])